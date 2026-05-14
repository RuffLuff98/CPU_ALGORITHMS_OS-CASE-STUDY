# Function that implements the Priority Round Robin
# CPU scheduling algorithm
from collections import deque

def priority_rr(processes, time_quantum):
    gantt = []
    current_time = 0
    # Initializes the remaining time of each process
    # for preemptive execution
    for p in processes:
        p.remaining_time = p.burst_time

    completed = 0
    n = len(processes)
    # Continues execution until all processes are completed
    while completed < n:

        ready = [
            p for p in processes
            if p.arrival_time <= current_time and p.remaining_time > 0
        ]
        if not ready:
            gantt.append("IDLE")
            current_time += 1
            continue
        highest_priority = min(p.priority for p in ready)
        same_priority = [
            p for p in ready if p.priority == highest_priority
        ]
        queue = deque(same_priority)
        # Executes processes inside the queue
        while queue:
            current = queue.popleft()
            if current.remaining_time == 0:
                continue
            exec_time = min(time_quantum, current.remaining_time)
            for _ in range(exec_time):
                gantt.append(current.pid)
                current_time += 1
                current.remaining_time -= 1
                ready_now = [
                    p for p in processes
                    if p.arrival_time <= current_time and p.remaining_time > 0
                ]
                for p in ready_now:
                    if p not in queue and p.priority == highest_priority and p != current:
                        queue.append(p)
                if current.remaining_time == 0:
                    break
            if current.remaining_time > 0:
                queue.append(current)
            else:
                current.completion_time = current_time
                current.turnaround_time = current.completion_time - current.arrival_time
                current.waiting_time = current.turnaround_time - current.burst_time
                completed += 1

    return processes, gantt