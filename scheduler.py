# Imports all available CPU scheduling algorithms
from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.srt import srt
from algorithms.rr import rr
from algorithms.priority import priority_scheduling
from algorithms.priority_rr import priority_rr


# Function responsible for selecting and executing
# the scheduling algorithm chosen by the user
def run_scheduler(choice, processes, time_quantum=None):

    choice = choice.upper()

    if choice == "FCFS":
        return fcfs(processes)

    elif choice == "SJF":
        return sjf(processes)

    elif choice == "SRT":
        return srt(processes)

    elif choice == "RR":
        if time_quantum is None:
            raise ValueError("Time quantum is required for Round Robin")
        return rr(processes, time_quantum)

    elif choice == "PRIORITY":
        return priority_scheduling(processes)

    elif choice == "PRIORITY_RR":
        if time_quantum is None:
            raise ValueError("Time quantum is required for Priority RR")
        return priority_rr(processes, time_quantum)

    else:
        raise ValueError("Invalid scheduling algorithm choice")