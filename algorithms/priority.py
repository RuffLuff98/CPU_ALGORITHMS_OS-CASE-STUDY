# Function that implements the non-preemptive
# Priority CPU Scheduling algorithm
def priority_scheduling(processes):
    processes = sorted(processes, key=lambda p: p.arrival_time)
    completed = []
    current_time = 0
    gantt = []
    # Continues execution until all processes are completed
    while len(completed) < len(processes):
        ready_queue = [
            p for p in processes
            if p not in completed and p.arrival_time <= current_time
        ]
        if not ready_queue:
            gantt.append("IDLE")
            current_time += 1
            continue
        current = min(ready_queue, key=lambda p: p.priority)
        current.start_time = current_time
        for _ in range(current.burst_time):
            gantt.append(current.pid)
            current_time += 1
        current.completion_time = current_time
        current.turnaround_time = current.completion_time - current.arrival_time
        current.waiting_time = current.turnaround_time - current.burst_time

        completed.append(current)

    return processes, gantt