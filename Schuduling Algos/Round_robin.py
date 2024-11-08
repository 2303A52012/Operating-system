from collections import deque

def round_robin_scheduling(processes, time_quantum):
    n = len(processes)
    remaining_times = {p: processes[p]['burst'] for p in processes}
    wait_times = {p: 0 for p in processes}
    turn_around_times = {p: 0 for p in processes}
    completion_times = {p: 0 for p in processes}
    current_time = 0
    queue = deque()
    processed = {p: False for p in processes}

    while True:
        all_done = True

        # Add all processes that have arrived and are not in the queue
        for p in processes:
            if processes[p]['arrival'] <= current_time and not processed[p]:
                queue.append(p)
                processed[p] = True
                all_done = False

        if all_done and not queue:
            break

        if queue:
            process = queue.popleft()
            execution_time = min(time_quantum, remaining_times[process])
            current_time += execution_time
            remaining_times[process] -= execution_time

            # Add newly arrived processes to the queue
            for p in processes:
                if processes[p]['arrival'] <= current_time and not processed[p]:
                    queue.append(p)
                    processed[p] = True

            if remaining_times[process] == 0:
                completion_times[process] = current_time
                turn_around_times[process] = completion_times[process] - processes[process]['arrival']
                wait_times[process] = turn_around_times[process] - processes[process]['burst']

            else:
                queue.append(process)

    return wait_times, turn_around_times, completion_times

# Input number of processes
n = int(input("Enter the number of processes: "))

# Input process details
processes = {}
print("Enter the arrival times and burst times for each process:")
for i in range(n):
    p_name = f"p{i+1}"
    arrival = int(input(f"Arrival time of {p_name}: "))
    burst = int(input(f"Burst time of {p_name}: "))
    processes[p_name] = {
        'arrival': arrival,
        'burst': burst
    }

# Input time quantum
time_quantum = int(input("Enter the time quantum: "))

# Call the Round Robin scheduling function
wait_times, turn_around_times, completion_times = round_robin_scheduling(processes, time_quantum)

# Output the results
print("\n---------------------------------------------------------------------------------------------------------")
print("Process\t  Arrival Time\t  Burst Time\t  Completion Time\t  Turnaround Time\t  Waiting Time")
for p in processes:
    print(f"  {p}\t\t{processes[p]['arrival']}\t\t{processes[p]['burst']}\t\t{completion_times[p]}\t\t\t{turn_around_times[p]}\t\t\t{wait_times[p]}")
print("---------------------------------------------------------------------------------------------------------")

# Calculate average waiting time and average turnaround time
avg_wait_time = sum(wait_times.values()) / len(wait_times)
avg_turn_around_time = sum(turn_around_times.values()) / len(turn_around_times)

# Output the averages
print(f"\nAverage Waiting Time: {avg_wait_time:.2f}")
print(f"Average Turnaround Time: {avg_turn_around_time:.2f}")