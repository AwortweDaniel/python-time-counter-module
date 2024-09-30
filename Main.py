import time



class SecondsCounter:
    def __init__(self, total_seconds):
        self.total_seconds = total_seconds
        self.countdown(self.total_seconds)

    def countdown(self, total_seconds):
        while total_seconds > 0:
            self.hours = total_seconds // 3600
            self.rem_seconds = total_seconds % 3600
            self.minutes = self.rem_seconds // 60
            self.seconds = self.rem_seconds % 60
            timer = "{:02d} : {:02d} : {:02d}".format(self.hours, self.minutes, self.seconds)
            print(timer)
            time.sleep(1)
            total_seconds -= 1

        print("Timeup!")


total_seconds = int(input("Enter the time in seconds: "))
time= SecondsCounter(total_seconds)

