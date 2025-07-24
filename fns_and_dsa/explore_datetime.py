import datetime

full_date = datetime.datetime.now()

def display_current_datetime():
    current_date = full_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")
    return current_date
   
display_current_datetime()

def calculate_future_date(future):
    future_date = full_date + datetime.timedelta(days=future)
    future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {future_date}")

calculate_future_date(int(input("Enter the number of days to add to the current date: ")))