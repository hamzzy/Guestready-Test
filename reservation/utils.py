import time

def validate_reservation_date(date1: str, date2: str)->bool:
    newdate1 = time.strptime(date1, "%Y-%m-%d")
    newdate2 = time.strptime(date2, "%Y-%m-%d")
    if  newdate2 > newdate1:
        return True
    elif newdate2 <= newdate1:
        return False
    

