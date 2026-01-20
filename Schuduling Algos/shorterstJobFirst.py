def sjf_scheduling(processes):
    n = len(processes)
    current_time = 0
    completed = 0

    for p in processes:
        p["CT"] = 0
        p["TAT"] = 0
        p["WT"] = 0
        p["done"] = False

    while completed < n:
        eligible = [p for p in processes if p["arrival"] <= current_time and not p["done"]]

        if not eligible:
            current_time += 1
            continue

        # pick shortest burst among available
        shortest = min(eligible, key=lambda x: x["burst"])

        current_time += shortest["burst"]
        shortest["CT"] = current_time
        shortest["TAT"] = shortest["CT"] - shortest["arrival"]
        shortest["WT"] = shortest["TAT"] - shortest["burst"]
        shortest["done"] = True
        completed += 1

    avg_wt = sum(p["WT"] for p in processes) / n
    avg_tat = sum(p["TAT"] for p in processes) / n

    print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
    for p in sorted(processes, key=lambda x: x["process"]):   # prints in P1,P2,P3 order
        print(f"{p['process']}\t{p['arrival']}\t{p['burst']}\t{p['CT']}\t{p['TAT']}\t{p['WT']}")

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Arrival time of P{i+1}: "))
    bt = int(input(f"Burst time of P{i+1}: "))
    processes.append({"process": f"P{i+1}", "arrival": at, "burst": bt})

sjf_scheduling(processes)
