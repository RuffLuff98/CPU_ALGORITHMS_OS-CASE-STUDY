# Imports deque for efficient queue operations
# used in Round Robin scheduling
from collections import deque
# Function that implements the Round Robin
# CPU scheduling algorithm
def rr(processes, time_quantum):
    queue = deque()
    gantt = []
    current_time = 0
    # Initializes remaining time for each process
    # for preemptive execution
    for p in processes:
        p.remaining_time = p.burst_time
    processes.sort(key=lambda p: p.arrival_time)
    i = 0
    n = len(processes)
    completed = 0
    # Continues execution until all processes are completed
    while completed < n:
        while i < n and processes[i].arrival_time <= current_time:
            queue.append(processes[i])
            i += 1
        if not queue:
            gantt.append("IDLE")
            current_time += 1
            continue
        current = queue.popleft()
        exec_time = min(time_quantum, current.remaining_time)
        for _ in range(exec_time):
            gantt.append(current.pid)
            current_time += 1
            current.remaining_time -= 1
            while i < n and processes[i].arrival_time <= current_time:
                queue.append(processes[i])
                i += 1
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