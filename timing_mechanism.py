import time

class TimingMechanism:
    def __init__(self, bpm):
        self.bpm = bpm
        self.start_time = time.time()

    def get_elapsed_beats(self):
        # Calculate the number of beats that have elapsed since the start of the song
        elapsed_seconds = time.time() - self.start_time
        elapsed_beats = elapsed_seconds / 60 * self.bpm
        return elapsed_beats

    def reset(self):
        # Reset the start time to the current time
        self.start_time = time.time()
