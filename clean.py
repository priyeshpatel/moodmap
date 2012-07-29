import moodmap
from apscheduler.scheduler import Scheduler

sched = Scheduler()

@sched.interval_schedule(minutes=15)
def clean():
    moodmap.clean()

if __name__ == '__main__':
    sched.start()
    while True:
        pass
