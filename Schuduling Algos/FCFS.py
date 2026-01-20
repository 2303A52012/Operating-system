p = []
n = int(input("Enter the number of processes: "))

for i in range(n):
    at = int(input(f"Enter Arrival Time of process {i+1}: "))
    bt = int(input(f"Enter Burst Time of process {i+1}: "))
    p.append({"process": i+1, "AT": at, "BT": bt})

# Sort by Arrival Time (FCFS Rule)
p.sort(key=lambda x: x["AT"])

for i in range(n):
    if i == 0:
        p[i]["CT"] = p[i]["AT"] + p[i]["BT"]
    else:
        p[i]["CT"] = max(p[i-1]["CT"], p[i]["AT"]) + p[i]["BT"]

    p[i]["TAT"] = p[i]["CT"] - p[i]["AT"]
    p[i]["WT"] = p[i]["TAT"] - p[i]["BT"]

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for pr in p:
    print(f"P{pr['process']}\t{pr['AT']}\t{pr['BT']}\t{pr['CT']}\t{pr['TAT']}\t{pr['WT']}")

total_wt = sum(pr["WT"] for pr in p)
avg_wt = total_wt / n
print(f"\nAverage Waiting Time = {avg_wt:.2f}")
