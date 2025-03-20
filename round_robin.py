def round_robin(processes, time_quantum):
    ready_queue = []
    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0

    while processes or ready_queue:
        while processes and processes[0].arrival_time <= current_time:
            ready_queue.append(processes.pop(0))
        
        if ready_queue:
            process = ready_queue.pop(0)
            if process.remaining_time > time_quantum:
                current_time += time_quantum
                process.remaining_time -= time_quantum
                ready_queue.append(process)  # Re-add to the queue if not finished
            else:
                current_time += process.remaining_time
                process.turnaround_time = current_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                total_turnaround_time += process.turnaround_time
                total_waiting_time += process.waiting_time
        else:
            current_time += 1  # Idle time

    average_turnaround_time = total_turnaround_time / 20
    average_waiting_time = total_waiting_time / 20

    return average_turnaround_time, average_waiting_time
