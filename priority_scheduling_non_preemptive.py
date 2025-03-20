def priority_scheduling_non_preemptive(processes):
    processes.sort(key=lambda p: (p.arrival_time, p.priority))  # Sort by arrival time, then by priority
    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0

    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time  # CPU idle until the process arrives
        process.waiting_time = current_time - process.arrival_time
        process.turnaround_time = process.burst_time + process.waiting_time
        process.completion_time = current_time + process.burst_time
        current_time += process.burst_time

        total_turnaround_time += process.turnaround_time
        total_waiting_time += process.waiting_time

    average_turnaround_time = total_turnaround_time / len(processes)
    average_waiting_time = total_waiting_time / len(processes)

    return average_turnaround_time, average_waiting_time
