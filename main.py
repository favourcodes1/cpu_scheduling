from fcfs import fcfs_scheduling
import multilevel_queue_scheduling
import priority_scheduling_non_preemptive
import priority_scheduling_preemptive
from process import generate_processes
import round_robin
import sjf_non_preemptive
import sjf_preemptive


def main():
    # Generate processes
    processes = generate_processes(20)
    
    # FCFS
    avg_tat_fcfs, avg_wt_fcfs = fcfs_scheduling(processes)
    print(f"FCFS - Average Turnaround Time: {avg_tat_fcfs}")
    print(f"FCFS - Average Waiting Time: {avg_wt_fcfs}")
    
    # SJF Non-Preemptive
    avg_tat_sjf_np, avg_wt_sjf_np = sjf_non_preemptive(processes)
    print(f"SJF Non-Preemptive - Average Turnaround Time: {avg_tat_sjf_np}")
    print(f"SJF Non-Preemptive - Average Waiting Time: {avg_wt_sjf_np}")
    
    # SJF Preemptive
    avg_tat_sjf_p, avg_wt_sjf_p = sjf_preemptive(processes)
    print(f"SJF Preemptive - Average Turnaround Time: {avg_tat_sjf_p}")
    print(f"SJF Preemptive - Average Waiting Time: {avg_wt_sjf_p}")
    
    # Round Robin
    time_quantum = 4  # Set a time quantum
    avg_tat_rr, avg_wt_rr = round_robin(processes, time_quantum)
    print(f"Round Robin - Average Turnaround Time: {avg_tat_rr}")
    print(f"Round Robin - Average Waiting Time: {avg_wt_rr}")
    
    # Priority Scheduling Non-Preemptive
    avg_tat_ps_np, avg_wt_ps_np = priority_scheduling_non_preemptive(processes)
    print(f"Priority Scheduling Non-Preemptive - Average Turnaround Time: {avg_tat_ps_np}")
    print(f"Priority Scheduling Non-Preemptive - Average Waiting Time: {avg_wt_ps_np}")
    
    # Priority Scheduling Preemptive
    avg_tat_ps_p, avg_wt_ps_p = priority_scheduling_preemptive(processes)
    print(f"Priority Scheduling Preemptive - Average Turnaround Time: {avg_tat_ps_p}")
    print(f"Priority Scheduling Preemptive - Average Waiting Time: {avg_wt_ps_p}")
    
    # Multilevel Queue Scheduling
    avg_tat_mqs, avg_wt_mqs = multilevel_queue_scheduling(processes, time_quantum)
    print(f"Multilevel Queue Scheduling - Average Turnaround Time: {avg_tat_mqs}")
    print(f"Multilevel Queue Scheduling - Average Waiting Time: {avg_wt_mqs}")

if __name__ == "__main__":
    main()
