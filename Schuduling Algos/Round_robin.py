from collections import deque

def round_robin_scheduling(processes, tq):
    n = len(processes)
    remaining = {p: processes[p]["burst"] for p in processes}
    CT = {p: 0 for p in processes}
    WT = {p: 0 for p in processes}
    TAT = {p: 0 for p in processes}

    current_time = 0
    queue = deque()
    added = {p: False for p in processes}

    while True:
        # add arrived processes
        for p in processes:
            if processes[p]["arrival"] <= current_time and not added[p]:
                queue.append(p)
                added[p] = True

        # stop when all completed
        if all(remaining[p] == 0 for p in remaining):
            break

        # CPU idle case
        if not queue:
            current_time += 1
            continue

        p = queue.popleft()

        exec_time = min(tq, remaining[p])
        current_time += exec_time
        remaining[p] -= exec_time

        # add newly arrived processes during this execution
        for x in processes:
            if processes[x]["arrival"] <= current_time and not added[x]:
                queue.append(x)
                added[x] = True

        if remaining[p] == 0:
            CT[p] = current_time
            TAT[p] = CT[p] - processes[p]["arrival"]
            WT[p] = TAT[p] - processes[p]["burst"]
        else:
            queue.append(p)

    return WT, TAT, CT


# -------- INPUT ----------
n = int(input("Enter number of processes: "))
processes = {}

for i in range(n):
    name = f"P{i+1}"
    at = int(input(f"Arrival time of {name}: "))
    bt = int(input(f"Burst time of {name}: "))
    processes[name] = {"arrival": at, "burst": bt}

tq = int(input("Enter time quantum: "))

WT, TAT, CT = round_robin_scheduling(processes, tq)

# -------- OUTPUT ----------
print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for p in processes:
    print(f"{p}\t{processes[p]['arrival']}\t{processes[p]['burst']}\t{CT[p]}\t{TAT[p]}\t{WT[p]}")

avg_wt = sum(WT.values()) / n
avg_tat = sum(TAT.values()) / n

print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
