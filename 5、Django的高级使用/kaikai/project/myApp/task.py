from celery import task
import time

@task
def sunck():
    print("sunck is a good man")
    time.sleep(5)
    print("sunck is a nice man")