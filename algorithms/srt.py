# Function that implements the Shortest Remaining Time (SRT)
# CPU scheduling algorithm (preemptive version of SJF)
def srt(processes):
    n = len(processes)
    completed = 0
    current_time = 0
    gantt = []
    for p in processes:
        p.remaining_time = p.burst_time
# Runs until all processes are completed
    while completed < n:
        ready = [
            p for p in processes
            if p.arrival_time <= current_time and p.remaining_time > 0
        ]
        if not ready:
            gantt.append("IDLE")
            current_time += 1
            continue
        current = min(ready, key=lambda p: p.remaining_time)
        gantt.append(current.pid)
        current.remaining_time -= 1
        current_time += 1
        if current.remaining_time == 0:
            current.completion_time = current_time
            current.turnaround_time = current.completion_time - current.arrival_time
            current.waiting_time = current.turnaround_time - current.burst_time
            completed += 1

    return processes, gantt