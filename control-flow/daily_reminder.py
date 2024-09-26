task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority :
    case 'high':
        if time_bound == 'yes' and priority == "high":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound == 'no' and priority == "high":
            print(f"Attension: '{task}' is a high priority task without time bound, consider completing time sensitive task before this, Thank you!")
    
    case 'medium' :
        if time_bound == 'yes' and priority == 'medium':
            print (f"'{task}', is a medium priority task, make sure you've handled all high priority tasks.")
        elif time_bound == 'no' and priority == 'medium':
            print(f"Note: '{task}' is a medium priority with no time bound, make sure you've completed all high priority task before working on this!")
    case "low":
        if time_bound == 'no' and priority == 'low':
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        elif time_bound == 'yes' and priority == 'low':
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
            print("No found task matching your input.")
