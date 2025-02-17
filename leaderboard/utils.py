from datetime import datetime, timedelta

date_time_format = "%Y-%m-%d %H:%M:%S"
def get_date_time_obj(date_time: str):
    return datetime.strptime(date_time, date_time_format)

def utc_date_time_now():
    return datetime.now() + timedelta(hours=5, minutes=30)