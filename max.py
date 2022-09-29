import uuid
from datetime import date

d = {str(uuid.uuid4()): [date(2022, 1, 1), 'blah'], str(uuid.uuid4()): [date(2022, 1, 2), 'blah123']}

# find max pair by date
max_record = max(d.values(), key=lambda x: x[0]) # where x[0] is a date