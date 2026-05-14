# Imports the required modules and functions for process creation,
# scheduling execution, and result display
from process import Process
from scheduler import run_scheduler
from utils import print_table, calculate_averages, print_gantt


# Function that safely accepts integer input and prevents
# invalid or negative values from being entered
def safe_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("!!! Value cannot be negative.")
                continue
            return value
        except ValueError:
            print("!!! Invalid input. Please enter a whole number.")


# Function responsible for collecting and validating
# all process information entered by the user
def get_processes():
    processes = []

    n = int(input("Enter number of processes (min 3): "))
    if n < 3:
        print("!!! Minimum 3 processes required.")
        return []

    # Loop used to create multiple process objects
    # containing PID, arrival time, burst time, and priority
    for i in range(n):
        print(f"\nProcess {i+1}")
        pid = "P" + input("PID number: ")
        at = safe_int("Arrival Time: ")

        # Ensures burst time is greater than zero
        while True:
         bt = safe_int("Burst Time: ")
         if bt > 0:
            break
         print("!!!Burst time cannot be 0. Try again.")

        pr = safe_int("Priority (lower number = higher priority): ")

        # Stores the created process object into the process list
        processes.append(Process(pid, at, bt, pr))

    return processes


# Main function that controls the overall flow of the program
def main():
    print("\n=== CPU Scheduling Program  ===")

    # Retrieves all user-defined processes
    processes = get_processes()

    # Displays available CPU scheduling algorithms
    print("\nChoose Algorithm:")
    print("FCFS, SJF, SRT, RR, PRIORITY, PRIORITY_RR")

    # Accepts the scheduling algorithm selected by the user
    choice = input("Enter choice: ").strip().upper()

    time_quantum = None

    # Requests a time quantum only for Round Robin based algorithms
    if choice in ["RR", "PRIORITY_RR"]:
        time_quantum = int(input("Enter Time Quantum: "))

    # Executes the selected scheduling algorithm
    result, gantt = run_scheduler(choice, processes, time_quantum)

    # Displays the computed scheduling results and Gantt chart
    print("\n=== PROCESS TABLE ===")
    print_table(result)

    print("\n=== AVERAGES ===")
    calculate_averages(result)

    print_gantt(gantt)


# Runs the main function when the program is executed
if __name__ == "__main__":
    main()

    import time

    while True:
        time.sleep(1)