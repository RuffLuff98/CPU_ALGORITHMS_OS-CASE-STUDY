# Class used to represent a single process in the CPU scheduling system
class Process:

    # Constructor that initializes all process attributes
    def __init__(self,pid,arrival_time,burst_time,priority=0):
        self.pid=pid
        self.arrival_time=arrival_time
        self.burst_time=burst_time
        self.priority=priority

        #for preemptive algos
        self.remaining_time=burst_time
        
        self.start_time=0
        self.completion_time=0
        self.waiting_time=0
        self.turnaround_time=0

   

