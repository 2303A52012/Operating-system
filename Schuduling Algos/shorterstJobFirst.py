def sjf_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: (x['arrival'], x['burst']))
    current_time = 0
    completed = 0
    wait_times = [0] * n
    turn_around_times = [0] * n
    completion_times = [0] * n
    is_completed = [False] * n

    while completed < n:
        min_burst = float('inf')
        selected_index = None

        for i in range(n):
            if (processes[i]['arrival'] <= current_time and not is_completed[i] and processes[i]['burst'] < min_burst):
                min_burst = processes[i]['burst']
                selected_index = i

        if selected_index is None:
            current_time += 1
            continue

        current_time += processes[selected_index]['burst']
        completion_times[selected_index] = current_time
        turn_around_times[selected_index] = completion_times[selected_index] - processes[selected_index]['arrival']
        wait_times[selected_index] = turn_around_times[selected_index] - processes[selected_index]['burst']
        is_completed[selected_index] = True
        completed += 1

    avg_wait_time = sum(wait_times) / n
    avg_turn_around_time = sum(turn_around_times) / n

    print("\nProcess\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for i in range(n):
        print(f"{processes[i]['process']}\t{processes[i]['burst']}\t\t{processes[i]['arrival']}\t\t{wait_times[i]}\t\t{turn_around_times[i]}\t\t{completion_times[i]}")

    print(f"\nAverage Waiting Time: {avg_wait_time:.2f}")
    print(f"Average Turnaround Time: {avg_turn_around_time:.2f}")

n = int(input("Enter the number of processes: "))
processes = []

for i in range(n):
    arrival = int(input(f"Arrival time of P{i+1}: "))
    burst = int(input(f"Burst time of P{i+1}: "))
    processes.append({'process':f"p{i+1}",'arrival': arrival, 'burst': burst})

sjf_scheduling(processes)
