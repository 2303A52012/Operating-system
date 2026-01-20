def priority_scheduling(processes):
    n = len(processes)

    wt = {p: 0 for p in processes}
    tat = {p: 0 for p in processes}
    ct = {p: 0 for p in processes}
    rem = {p: processes[p]['burst'] for p in processes}
    done = {p: False for p in processes}

    current_time = 0
    completed = 0

    while completed < n:
        selected = None
        min_priority = float("inf")

        for p in processes:
            if processes[p]["arrival"] <= current_time and not done[p]:
                if processes[p]["priority"] < min_priority:
                    min_priority = processes[p]["priority"]
                    selected = p
                elif processes[p]["priority"] == min_priority:
                    # tie-breaker: earlier arrival
                    if selected is None or processes[p]["arrival"] < processes[selected]["arrival"]:
                        selected = p

        if selected is None:
            current_time += 1
            continue

        # execute 1 unit time (preemptive)
        rem[selected] -= 1
        current_time += 1

        if rem[selected] == 0:
            done[selected] = True
            completed += 1
            ct[selected] = current_time
            tat[selected] = ct[selected] - processes[selected]["arrival"]
            wt[selected] = tat[selected] - processes[selected]["burst"]

    return wt, tat, ct


n = int(input("Enter number of processes: "))
processes = {}

for i in range(n):
    name = f"P{i+1}"
    at = int(input(f"Arrival time of {name}: "))
    bt = int(input(f"Burst time of {name}: "))
    pr = int(input(f"Priority of {name} (lower = higher): "))
    processes[name] = {"arrival": at, "burst": bt, "priority": pr}

wt, tat, ct = priority_scheduling(processes)

print("\nProcess\tAT\tBT\tPR\tCT\tTAT\tWT")
for p in processes:
    print(f"{p}\t{processes[p]['arrival']}\t{processes[p]['burst']}\t{processes[p]['priority']}\t{ct[p]}\t{tat[p]}\t{wt[p]}")

avg_wt = sum(wt.values()) / n
avg_tat = sum(tat.values()) / n
print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
