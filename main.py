# CPU Scheduling Simulator in CLI
from process import Process 
# First input must contain 3 numbers:
# [Algorithm, Number of Processes, Quantum]

#   Algorithms
#   0 - First-Come-First-Serve (FCFS)
#   1 - Shortest-Job-First (SJF)
#   2 - Shortest-Remaining-Time-First (SRTF)
#   3 - Round-Robin (RR)

algorithm = -1
num_processes = 0
quantum = 0

processes = []
queue = []

# Main
start_input = input().split()

algorithm = int(start_input[0])
num_processes = int(start_input[1])
quantum = int(start_input[2])

# Get processes
for i in range(num_processes):
    process_input = input().split()
    processes.append(Process(i, int(process_input[0]), int(process_input[1])))