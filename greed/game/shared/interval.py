from datetime import datetime

class SetInterval:
    """SetInterval calls a function at set intervals until the interval gets to a end time"""    
    def __init__(self):
        pass
        
    
    def set_interval(self,event, interval=1, end=20):
        """SetInterval calls a function at set intervals until the interval gets to a end time
        
        Args:
        event(function): A function (NOT A FUNCTION CALL)
        interval(int): intervals in seconds between each function call
        end(int): Duration of function"""
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        hour = datetime.now().hour
        minute = datetime.now().minute
        second = datetime.now().second
        microsecond = datetime.now().microsecond

        cur_time = datetime(year ,month ,day, hour, minute, second, microsecond).timestamp()
        next_time = cur_time + interval
        end_time = 0
        while end_time < end:
            
            year = datetime.now().year
            month = datetime.now().month
            day = datetime.now().day
            hour = datetime.now().hour
            minute = datetime.now().minute
            second = datetime.now().second
            microsecond = datetime.now().microsecond
            new_time = datetime(year ,month ,day, hour, minute, second, microsecond).timestamp()

            if new_time >= next_time:
                next_time += interval
                # Events
                event()
                end_time += interval



