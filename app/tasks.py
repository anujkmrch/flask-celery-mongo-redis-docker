from app import celery
from app.models import User

@celery.task
def save_user_to_db(name, email):
    user = User(name=name, email=email)
    user.save()
    # Trigger Task B from within Task A
    result_b = task_b.delay(f"Data from Task A: {user.to_json()}")
    return user.to_json()
    
    
@celery.task
def task_b(data):
    """Dependent task (Task B)"""
    print(f"Task B received: {data}")
    return f"Processed {data} in Task B"
