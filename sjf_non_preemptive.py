def sjf_non_preemptive(processes):
    processes.sort(key=lambda p: (p.arrival_time, p.burst_time))
    completed = []
    current_time = 0
    
    while len(completed) < len(processes):
        ready_queue = [p for p in processes if p.arrival_time <= current_time and p not in completed]
        if ready_queue:
            next_process = min(ready_queue, key=lambda p: p.burst_time)
            current_time += next_process.burst_time
            next_process.completion_time = current_time
            next_process.turnaround_time = next_process.completion_time - next_process.arrival_time
            next_process.waiting_time = next_process.turnaround_time - next_process.burst_time
            completed.append(next_process)
        else:
            current_time += 1

    average_turnaround_time = sum(p.turnaround_time for p in completed) / len(completed)
    average_waiting_time = sum(p.waiting_time for p in completed) / len(completed)

    return average_turnaround_time, average_waiting_time
