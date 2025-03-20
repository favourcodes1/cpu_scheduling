def multilevel_queue_scheduling(processes, time_quantum):
    high_priority_queue = [p for p in processes if p.priority <= 2]  # Assume priority 1 and 2 are high priority
    low_priority_queue = [p for p in processes if p.priority > 2]    # Assume priority 3-5 are low priority
    
    # Apply Round Robin to the high-priority queue
    avg_tat_rr, avg_wt_rr = round_robin(high_priority_queue, time_quantum)
    
    # Apply FCFS to the low-priority queue
    avg_tat_fcfs, avg_wt_fcfs = fcfs_scheduling(low_priority_queue)
    
    # Calculate the combined average turnaround time and waiting time
    total_processes = len(processes)
    avg_tat = (avg_tat_rr * len(high_priority_queue) + avg_tat_fcfs * len(low_priority_queue)) / total_processes
    avg_wt = (avg_wt_rr * len(high_priority_queue) + avg_wt_fcfs * len(low_priority_queue)) / total_processes
    
    return avg_tat, avg_wt
