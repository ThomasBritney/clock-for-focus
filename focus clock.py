import time

def focus_timer(mins):
    startTime = time.time()
    endTime = startTime + mins*60

    while time.time() < endTime:
        remaining_time = endTime - time.time()
        mins, secs = divmod(remaining_time, 60)
        timer = '{:02d}:{:02d}'.format(int(mins), int(secs))
        print("Time remaining: "+timer,end="\r")
        time.sleep(1)

    print("Time's up! You can take a break now.")

# Example usage, sets focus timer for 25 minutes (1500 seconds)
focus_timer(25)
