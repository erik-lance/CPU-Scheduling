class Process:
    def __init__(self, id, arrival_time, burst_time):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_end_time = []
        self.is_processed = False

    def set_processed(self):
        """Sets the process as processed."""
        self.is_processed = True

    def add_start_end_time(self, start_time, end_time):
        """Adds a tuple of start and end time to the list of start and end times. Also subtracts the time from the remaining time.

        :param start_time: The start time of the process.
        :param end_time: The end time of the process.
        """
        self.start_end_time.append((start_time, end_time, self.remaining_time))
        self.remaining_time -= end_time - start_time

    def get_start_end_time_string(self):
        """Returns a string of the start and end times of the process.

        :return: Formatted string of the start and end times for final output.
        """
        if len(self.start_end_time) == 0:
            return "No start and end times."

        # Prints as "start time: X end time: Y | start time: X end time: Y | ..."
        time_string = []
        for start_time, end_time, remaining_time in self.start_end_time:
            waiting_time = end_time - self.arrival_time - self.burst_time
            time_string.append(
                f"{self.id} start time: {start_time} end time: {end_time} | Waiting time: {waiting_time if waiting_time > 0 else 0}"
            )

        return "\n".join(time_string)

    def get_turnaround_time(self):
        """Calculates the turnaround time of the process.

        :return: The turnaround time of the process.
        """

        # Turnaround time = End time - Arrival time
        # Get last end time
        end_time = self.start_end_time[-1][1]
        return end_time - self.arrival_time

    def get_waiting_time(self):
        """Calculates the waiting time of the process.

        :return: The waiting time of the process.
        """

        # Waiting time = Turnaround time - Burst time
        ret = self.get_turnaround_time() - self.burst_time
        return 0 if ret < 0 else ret

    def __str__(self):
        if self.remaining_time == 0:
            # Present individual start and end times
            return self.get_start_end_time_string()
        else:
            # Present debugging information
            return f"FAILED - {self.id} AT: {self.arrival_time} BT: {self.burst_time} \nRemaining Time: {self.remaining_time}\nTimes: {self.get_start_end_time_string()}\n"
