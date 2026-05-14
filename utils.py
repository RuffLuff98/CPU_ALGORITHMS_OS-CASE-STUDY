# Function used to display the process information
# in a formatted table structure
def print_table(processes):
    print("\n{:<10}{:<10}{:<10}{:<12}{:<12}{:<15}".format(
        "Process", "Burst", "Priority", "Arrival", "Waiting", "Turnaround"
    ))

    print("-" * 75)
    # Loops through all processes and displays
    # their scheduling information
    for p in processes:
        print("{:<10}{:<10}{:<10}{:<12}{:<12}{:<15}".format(
            p.pid,
            p.burst_time,
            p.priority,
            p.arrival_time,
            p.waiting_time,
            p.turnaround_time
        ))

# Function responsible for calculating and displaying
# the average waiting time and turnaround time
def calculate_averages(processes):
    total_wt = 0
    total_tat = 0
    n = len(processes)

    for p in processes:
        total_wt += p.waiting_time
        total_tat += p.turnaround_time

    avg_wt = total_wt / n
    avg_tat = total_tat / n

    print("\n--- Averages ---")
    print("Average Waiting Time:", round(avg_wt, 2))
    print("Average Turnaround Time:", round(avg_tat, 2))

# Function used to display the Gantt chart
# showing the execution order of processes
def print_gantt(gantt):
    print("\n--- Gantt Chart (Step-by-step) ---")
    print("Time: ", end="")
    for i in range(len(gantt) + 1):
        print(f"{i}    ", end="")
    print("\n      |" + "-----|" * len(gantt))
    print("      |", end="")
    for p in gantt:
        print(f" {p:<3} |", end="")
    print("\n")
    