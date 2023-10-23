# CPU Scheduling Simulator in CLI
from calendar import c
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

# Get total burst time
total_burst_time = 0
for process in processes:
    total_burst_time += process.burst_time
total_burst_time += 1  # Add 1 to account for last process

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
    start_time = 0
    is_running = False
    next_process_time = -1

    for i in range(total_burst_time):
        print(f"Time: {i}")
        # Check if process arrives
        for process in processes:
            if process.arrival_time == i:
                print(f"Process {process.id} arrived.")
                queue.append(process)

        # If next process time is reached, set is_running to False
        if i == next_process_time:
            print(f"Process {queue[0].id} finished.")
            is_running = False
            queue[0].add_start_end_time(start_time, i)
            print(
                f"Process {queue[0].id} start time: {start_time} end time: {i} remaining time: {queue[0].remaining_time}"
            )

        # If a process is running (no interrupt), skip to next iteration
        if is_running:
            print(f"Process {queue[0].id} is running. Ends at {next_process_time}.")
            continue

        # Check if there's next in queue
        if len(queue) > 1:
            print(f"Process {queue[1].id} is next.")
            # Check if next process has arrived, re-append to queue if current process is not finished
            if queue[1].arrival_time <= i:
                print(f"Process {queue[0].id} re-append.")
                current_process = queue.pop(0)
                if current_process.remaining_time > 0:
                    queue.append(current_process)

            print(f"Process {queue[0].id} is running.")
            is_running = True
            start_time = i
            next_process_time = (
                i + quantum
                if queue[0].remaining_time > quantum
                else i + queue[0].remaining_time
            )
        else:
            print(f"Process {queue[0].id} is running.")
            is_running = True
            start_time = i
            next_process_time = (
                i + quantum
                if queue[0].remaining_time > quantum
                else i + queue[0].remaining_time
            )


# Print output
for process in processes:
    print(process)
    print(
        "Average waiting time:",
        sum([process.get_waiting_time() for process in processes]) / len(processes),
    )
