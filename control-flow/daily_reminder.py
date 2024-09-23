task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is is time-bound? (yes/no): ")
match task :
    case '1':
        if priority == 'high' and time == 'yes':
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case '2' :
        if priority == "medium" and time == "yes" :
            print ("f{task}, is of medium on your list, do make sure you've handled the high priority tasks")

