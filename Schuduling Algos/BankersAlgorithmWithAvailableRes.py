p = []  
r = []  

n = int(input("Enter the number of processes: "))
nr = int(input("Enter the number of resources: "))

for i in range(nr):
    r.append(input(f"Enter the {i+1}th resource name: "))

for i in range(n):
    A = []    
    MN = []   
    R = []    

    for j in range(nr):
        A.append(int(input(f"Enter the allocated resources for {r[j]} of Process {i+1}: ")))
    for j in range(nr):
        MN.append(int(input(f"Enter the Max needed resources for {r[j]} of Process {i+1}: ")))
    for j in range(nr):
        R.append(MN[j] - A[j])  

    process = {
        "process": i + 1,
        "allocated": A,
        "maxNeed": MN,
        "required": R,
        "finished": False  
    }
    p.append(process)

available = []
for i in range(nr):
    available.append(int(input(f"Enter the currently available units for resource {r[i]}: ")))

def can_execute(process, available):
    for i in range(nr):
        if process["required"][i] > available[i]:
            return False
    return True

safe_sequence = []
finished_processes = 0

while finished_processes < n:
    executed_process = False
    for process in p:
        if not process["finished"] and can_execute(process, available):
            for i in range(nr):
                available[i] += process["allocated"][i]
            process["finished"] = True
            safe_sequence.append(process["process"])
            finished_processes += 1
            executed_process = True

    if not executed_process:
        print("The system is in an unsafe state!")
        break
else:
    print("The system is in a safe state.")
    print("Safe sequence is:", safe_sequence)

print("\nProcesses details:")
for process in p:
    print(f"Process {process['process']}: Allocated {process['allocated']}, MaxNeed {process['maxNeed']}, Required {process['required']}")