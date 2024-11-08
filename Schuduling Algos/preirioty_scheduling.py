def priority_scheduling(processes):
    n = len(processes)
    wait_times = {p: 0 for p in processes}
    turn_around_times = {p: 0 for p in processes}
    completion_times = {p: 0 for p in processes}
    remaining_bursts = {p: processes[p]['burst'] for p in processes}
    is_completed = {p: False for p in processes}
    current_time = 0
    completed = 0

    while completed < n:
        min_priority = float('inf')
        selected_process = None

        for p in processes:
            if (processes[p]['arrival'] <= current_time and not is_completed[p] and processes[p]['priority'] < min_priority):
                min_priority = processes[p]['priority']
                selected_process = p
            elif (processes[p]['arrival'] <= current_time and not is_completed[p] and processes[p]['priority'] == min_priority and processes[p]['arrival'] < processes[selected_process]['arrival']):
                selected_process = p

        if selected_process is None:
            current_time += 1
            continue

        remaining_bursts[selected_process] -= 1
        current_time += 1

        if remaining_bursts[selected_process] == 0:
            is_completed[selected_process] = True
            completed += 1
            completion_times[selected_process] = current_time
            turn_around_times[selected_process] = completion_times[selected_process] - processes[selected_process]['arrival']
            wait_times[selected_process] = turn_around_times[selected_process] - processes[selected_process]['burst']

    return wait_times, turn_around_times, completion_times

n = int(input("Enter the number of processes: "))

processes = {}

print("Enter the arrival times, burst times, and priority for each process:")

for i in range(n):
    p_name = f"p{i+1}"
    arrival = int(input(f"Arrival time of {p_name}: "))
    burst = int(input(f"Burst time of {p_name}: "))
    priority = int(input(f"Priority of {p_name} (lower value = higher priority): "))
    processes[p_name] = {
        'arrival': arrival,
        'burst': burst,
        'priority': priority
    }

wait_times, turn_around_times, completion_times = priority_scheduling(processes)

print("\nProcess\tBurst Time\tArrival Time\tPriority\tWaiting Time\tTurnaround Time\tCompletion Time")

for p in processes:
    print(f"{p}\t{processes[p]['burst']}\t\t{processes[p]['arrival']}\t\t{processes[p]['priority']}\t\t{wait_times[p]}\t\t{turn_around_times[p]}\t\t{completion_times[p]}")

avg_wait_time = sum(wait_times.values()) / len(wait_times)
avg_turn_around_time = sum(turn_around_times.values()) / len(turn_around_times)

print(f"\nAverage Waiting Time: {avg_wait_time:.2f}")
print(f"Average Turnaround Time: {avg_turn_around_time:.2f}")