class Process:
    def __init__(self, id, arrival_time, burst_time):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_end_time = []
        self.waiting_time = 0
    
    def add_start_end_time(self, start_time, end_time):
        """Adds a tuple of start and end time to the list of start and end times. Also subtracts the time from the remaining time.

        :param start_time: The start time of the process.
        :param end_time: The end time of the process.
        """
        self.start_end_time.append((start_time, end_time))
        self.remaining_time -= (end_time - start_time)

    def get_start_end_time_string(self):
        """Returns a string of the start and end times of the process.

        :return: Formatted string of the start and end times for final output.
        """
        
        # Prints as "start time: X end time: Y | start time: X end time: Y | ..."
        time_string = ""
        for start_time, end_time in self.start_end_time:
            time_string += f"start time: {start_time} end time: {end_time} | "
        
        return time_string[:-3] # Remove last " | "

    def __str__(self):
        return f"{self.id} {self.get_start_end_time_string} | Waiting Time: {self.waiting_time}"

