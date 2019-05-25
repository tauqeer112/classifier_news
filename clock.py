
import subprocess


def my_interval_job1():
    subprocess.call(['python', 'classifier.py'])


if __name__ == '__main__':
    from apscheduler.schedulers.blocking import BlockingScheduler
    sched = BlockingScheduler()

    sched.add_job(my_interval_job1, 'interval', id='classifier',      hours=24)
    sched.start()
