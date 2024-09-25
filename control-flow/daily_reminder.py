task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority :
    case 'high':
        if priority == 'high' and time_bound == 'yes':
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case 'medium' :
        if priority == "medium" and time_bound == "yes" :
            print (f"{task}, is a medium priority task, make sure you've handled all high priority tasks.")
    case "low":
        if priority == "low" and time_bound == "no" :
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
            print("No found task matching your input.")
