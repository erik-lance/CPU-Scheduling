from process import Process

class Debug:
    """This class contains debug inputs for testing purposes.
    """
    def __init__(self):
        pass
    
    def sample_1(self, algorithm=-1, quantum=1):
        """This sample input is taken from CPU Scheduling Exercise without priority.
        """
        processes = []
        processes.append(Process(1, 1, 20))
        processes.append(Process(2, 3, 4))
        processes.append(Process(3, 8, 6))
        processes.append(Process(4, 11, 12))
        
        if algorithm != -1:
            return algorithm, processes, quantum
        else:
            return processes