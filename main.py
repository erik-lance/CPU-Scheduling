# CPU Scheduling Simulator in CLI
import sys
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

# Add Input File to Debug
# e.g.: debug = 'input_files/sample.txt'
debug = 'input_files/sample.txt'

if debug is not None:
    sys.stdin = open(debug, 'r')

# Main
start_input = input().split()

# Check if valid
if len(start_input) != 3:
    print("Invalid input.")
    exit(1)
else:
    algorithm = int(start_input[0])
    num_processes = int(start_input[1])
    quantum = int(start_input[2])

# Check if valid
if algorithm not in range(4):
    print("Invalid algorithm.")
    exit(1)
elif num_processes < 3 and num_processes > 100:
    print("Invalid number of processes.")
    exit(1)
elif quantum < 1 and quantum > 100:
    print("Invalid quantum.")
    exit(1)

# Get processes
for i in range(num_processes):
    process_input = input().split()
    if len(process_input) != 3:
        print("Invalid input.")
        exit(1)
    else:
        processes.append(Process(int(process_input[0]), int(process_input[1]), int(process_input[2])))


# Run algorithm
queue = []

if algorithm == 0:
    # FCFS
    pass
elif algorithm == 1:
    # SJF
    pass
elif algorithm == 2:
    # SRTF
    pass
elif algorithm == 3:
    # Round Robin
    pass


# Print output
for process in processes:
    print(process)