# Function that implements the First Come First Serve (FCFS)
# CPU scheduling algorithm
def fcfs(processes):
    # Sorts processes based on arrival time
    # so the earliest arriving process executes first
    processes.sort(key=lambda p: p.arrival_time)

    current_time = 0
    gantt = []

    # Loops through all processes in arrival order
    for p in processes:
        while current_time < p.arrival_time:
            gantt.append("IDLE")
            current_time += 1
        p.start_time = current_time
        for _ in range(p.burst_time):
            gantt.append(p.pid)
            current_time += 1
        p.completion_time = current_time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

    return processes, gantt