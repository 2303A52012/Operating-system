p = []
n = int(input("Enter the number of processes: "))
for i in range(n):
    process = {
        "process": i + 1,
        "AT": int(input(f"Enter the Arrival Time of process {i+1}: ")),
        "BT": int(input(f"Enter the Burst Time of process {i+1}: "))
    }
    p.append(process)  

# Sort the processes by Arrival Time (AT)
p.sort(key=lambda process: process['AT'])

# Calculate Completion Time (CT), Turnaround Time (TAT), and Waiting Time (WT)
for i in range(n):
    if i == 0:
        p[i]["CT"] = p[i]["AT"] + p[i]["BT"]
    else:
        p[i]["CT"] = max(p[i-1]["CT"], p[i]["AT"]) + p[i]["BT"]

    p[i]["TAT"] = p[i]["CT"] - p[i]["AT"]  # Turnaround Time
    p[i]["WT"] = p[i]["TAT"] - p[i]["BT"]  # Waiting Time

for process in p:
    print(f"Process {process['process']}:")
    print(f"  Arrival Time (AT): {process['AT']}")
    print(f"  Burst Time (BT): {process['BT']}")
    print(f"  Completion Time (CT): {process['CT']}")
    print(f"  Turnaround Time (TAT): {process['TAT']}")
    print(f"  Waiting Time (WT): {process['WT']}")
    print()

#find the average waiting time ...
sum=0
for i in range(n):
    sum+=p[i]["WT"]
print(f"the average  watiting time of the all processes is {float(sum)/float(n)}")