from celery import shared_task
import time

@shared_task
def process_feedback(feedback_id):
    time.sleep(5)  # simulate long processing
    print(f"Feedback {feedback_id} processed!")
