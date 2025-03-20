def priority_scheduling_preemptive(processes):
    current_time = 0
    completed = []
    ready_queue = []

    while len(completed) < len(processes):
        # Add processes that have arrived
        ready_queue += [p for p in processes if p.arrival_time == current_time]
        ready_queue = [p for p in ready_queue if p.remaining_time > 0]  # Filter unfinished processes
        
        if ready_queue:
            ready_queue.sort(key=lambda p: p.priority)  # Sort by priority
            next_process = ready_queue[0]
            next_process.remaining_time -= 1  # Simulate execution

            if next_process.remaining_time == 0:
                next_process.completion_time = current_time + 1
                next_process.turnaround_time = next_process.completion_time - next_process.arrival_time
                next_process.waiting_time = next_process.turnaround_time - next_process.burst_time
                completed.append(next_process)
        
        current_time += 1

    average_turnaround_time = sum(p.turnaround_time for p in completed) / len(completed)
    average_waiting_time = sum(p.waiting_time for p in completed) / len(completed)

    return average_turnaround_time, average_waiting_time
