from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print(f"Current time and date:",current_date.strftime('%Y-%m-%d %H:%M'))

    def calculate_future_date():
        count_days = int(input("Enter the number of days to add to the current date: "))
        tdelta = timedelta(days=count_days)
        future_date = current_date + tdelta
        print(f"Future date:",future_date.strftime('%Y-%m-%d %H:%M'))


    calculate_future_date()
display_current_datetime()