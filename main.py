# CPU Scheduling Simulator in CLI
from calendar import c
import sys

from numpy import minimum
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
debug = "input_files/sample.txt"

if debug is not None:
    sys.stdin = open(debug, "r")

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
        processes.append(
            Process(int(process_input[0]), int(process_input[1]), int(process_input[2]))
        )


# For debugging purposes
def print_queue(queue):
    print("Queue:")
    for process in queue:
        print(f"Process {process.id} remaining time: {process.remaining_time}")


# Run algorithm
queue = []

if algorithm == 0:
    # FCFS
    start_time = 0
    end_time = 0
    i = 0
    # While there is at least one process that is not processed
    while not all([process.is_processed for process in processes]):
        for process in processes:
            if process.arrival_time == i:
                queue.append(process)
                # The end time of the current process is the burts time adedd with its start time
                end_time = start_time + process.burst_time
                process.add_start_end_time(start_time, end_time)
                # The start time of the next process is the current end time
                start_time = end_time
                process.set_processed()
        i += 1
    pass
elif algorithm == 1:
    # SJF
    pass
elif algorithm == 2:
    # SRTF
    start_time = 0
    is_running = -1
    next_process_time = -1
    i = 0
    # While there is at least one process that is not processed
    while not all([process.is_processed for process in processes]):
        for process in processes:
            if process.arrival_time == i:
                # print(f"Process {process.id} arrived.")
                queue.append(process)
        
        lowest = -1
        counter = 0
        for process in queue:
            if lowest == -1 or (queue[counter].remaining_time() < queue[lowest].remaining_time() and queue[counter].remaining_time() > 0):
                lowest = counter
            counter += 1
        if is_running == -1:
            is_running = lowest
        
        if lowest != is_running:
            queue[is_running].add_start_end_time(start_time, i)
            if queue[is_running].remaining_time == 0:
                queue[is_running].set_processed()
                queue.pop(is_running)
            is_running = lowest
            start_time = i
        i += 1
    pass
elif algorithm == 3:
    # Round Robin
    start_time = 0
    is_running = False
    next_process_time = -1
    i = 0
    # While there is at least one process that is not processed
    while not all([process.is_processed for process in processes]):
        # print(f"Time: {i}")
        # Check if process arrives
        for process in processes:
            if process.arrival_time == i:
                # print(f"Process {process.id} arrived.")
                queue.append(process)

        # If next process time is reached, set is_running to False
        if i == next_process_time:
            # print(f"Process {queue[0].id} finished.")
            is_running = False
            queue[0].set_processed()
            queue[0].add_start_end_time(start_time, i)
            # print(f"Process {queue[0].id} start time: {start_time} end time: {i} remaining time: {queue[0].remaining_time}")

            # Remove process from queue if remaining time is 0
            # Else, append to end of queue
            if queue[0].remaining_time == 0:
                queue.pop(0)
            else:
                queue.append(queue.pop(0))

            # print_queue(queue)

        # If a process is running (no interrupt), skip to next iteration
        # If queue is empty, skip to next iteration
        if is_running or len(queue) == 0:
            i += 1
            continue

        # print(f"Process {queue[0].id} is running.")
        is_running = True
        start_time = i
        next_process_time = (
            i + quantum
            if queue[0].remaining_time > quantum
            else i + queue[0].remaining_time
        )
        i += 1

# Print output
for process in processes:
    print(process)

print(
    "Average waiting time:",
    sum([process.get_waiting_time() for process in processes]) / len(processes),
)
