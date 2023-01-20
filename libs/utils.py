from uuid import uuid4
from datetime import datetime



def generate_id():
    id = str(uuid4())
    return id


def now():
    return datetime.now()