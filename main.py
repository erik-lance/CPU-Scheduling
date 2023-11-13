# CPU Scheduling Simulator in CLI
import os
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
debug = None

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
elif num_processes < 3 or num_processes > 100:
    print("Invalid number of processes. Is ", num_processes, "Must be between 3 and 100 (inclusive).")
    exit(1)
elif quantum < 1 or quantum > 100:
    print("Invalid quantum. Is ", quantum, "Must be between 1 and 100 (inclusive).")
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
    # The start time should be the arrival time of the first process to arrive
    # Find the first process to arrive
    start_time = -1
    for process in processes:
        if start_time == -1 or process.arrival_time < start_time:
            start_time = process.arrival_time

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

elif algorithm == 1:
    # SJF

    # Find the first process to arrive
    start_time = -1
    for process in processes:
        if start_time == -1 or process.arrival_time < start_time:
            start_time = process.arrival_time

    end_time = start_time
    i = 0
    arrived = []
    # While there is at least one process that is not processed
    while not all([process.is_processed for process in processes]):
        for process in processes:
            if process.arrival_time == i:
                queue.append(process)

            # when queue is ready
            if len(queue) == len(processes):
                for process in queue:
                    # checks for processes that arrived while the previous process was executing
                    if end_time >= process.arrival_time and not process.is_processed:
                        arrived.append(process)

                if len(arrived) > 0:
                    # sort already arrived processes by burst time
                    arrived.sort(key=lambda x: x.burst_time)

                    end_time = start_time + arrived[0].burst_time
                    arrived[0].add_start_end_time(start_time, end_time)
                    start_time = end_time
                    arrived[0].set_processed()
                    arrived = []
        i += 1

elif algorithm == 2:
    # SRTF
    start_time = 0
    is_running = -1
    next_process_time = -1
    i = 0
    # While there is at least one process that is not processed
    while not all([process.is_processed for process in processes]):
        # Adds the process to the queue if it arrives at the current time
        for process in processes:
            if process.arrival_time == i:
                # print(f"Process {process.id} arrived.")
                queue.append(process)

        lowest = -1
        counter = 0
        # Gets the index of the process in the queue with the lowest remaining time
        for process in queue:
            if lowest == -1 or (
                lowest != -1
                and queue[counter].remaining_time < queue[lowest].remaining_time
                and queue[counter].remaining_time > 0
            ):
                lowest = counter
            counter += 1
        if is_running == -1:
            is_running = lowest
            start_time = i
        # checks if the remaining unupdated time of the process is less than the lowest remaining time of a process in the queue
        if (
            is_running != -1
            and queue[is_running].remaining_time - (i - start_time)
            < queue[lowest].remaining_time
        ):
            lowest = is_running
        # print(lowest)
        # print(is_running)
        if is_running != -1 and lowest != -1:
            if (
                lowest != is_running
                or (i - start_time) == queue[is_running].remaining_time
            ):
                queue[is_running].add_start_end_time(start_time, i)
                # if the process is finished, remove it from the queue and set process as processed
                if queue[is_running].remaining_time == 0:
                    queue[is_running].set_processed()
                    queue.pop(is_running)
                    lowest = -1
                    counter = 0
                    # Gets the index of the process in the queue with the lowest remaining time
                    for process in queue:
                        if lowest == -1 or (
                            lowest != -1
                            and queue[counter].remaining_time
                            < queue[lowest].remaining_time
                            and queue[counter].remaining_time > 0
                        ):
                            lowest = counter
                        counter += 1
                    is_running = lowest
                else:
                    is_running = lowest
                start_time = i
        # print_queue(queue)
        i += 1

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
            queue[0].add_start_end_time(start_time, i)
            # print(f"Process {queue[0].id} start time: {start_time} end time: {i} remaining time: {queue[0].remaining_time}")

            # Remove process from queue if remaining time is 0
            # Else, append to end of queue
            if queue[0].remaining_time == 0:
                queue.pop(0).set_processed()
            else:
                queue.append(queue.pop(0))

            # Print queue for debugging
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

# Clear console using cls
os.system("cls")

# Print output in order of process id
for process in sorted(processes, key=lambda x: x.id):
    print(process.get_start_end_time_string())

print(
    "Average waiting time:",
    sum([process.get_waiting_time() for process in processes]) / len(processes),
)

# Save output to file
sys.stdout = open("output.txt", "w")
