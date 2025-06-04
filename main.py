from shift_planner import ShiftPlanner, load_previous_weeks
import sys

def menu():
    print("\n=== Automatic Shift Scheduler ===")
    print("\n1. Generate Schedule")
    print("2. Display Schedule")
    print("3. Export to CSV")
    print("4. Export to Excel")
    print("5. Request Staff Leave")
    print("0. Exit")
    
    return input("Select an option: ")

def get_inputs(): 
    week_number = int(input("Enter the week number you are planning for "))
    m = int(input("Enter number of staff members (m): "))
    n = 7 # Weekly schedule, so always 7 days
    k = int(input("Enter minimum off-days oer staff(k): "))
    print("Enter daily minimum staff requirement (space-separated for each day): ")
    daily = list(map(int, input().strip().split()))
    assert len(daily) == n, "You must enter a requirement for each day."



    previous_weeks = []
    while True: 
        path =input("Enter path to a previous week's schedule (or press enter to stop)")
        if not path.strip():
            break
        previous_weeks.append(path.strip())

    return m, n, k, daily, week_number, previous_weeks; 

def main():
    planner = None
    
    while True:
        choice = menu()
        
        match choice:
            case "1":
                m, n, k, daily, week_number, previous_weeks = get_inputs()
                # Ask user for previous files
                history = load_previous_weeks(previous_weeks, m, n)
                planner = ShiftPlanner(m, n, k, daily, history)
                planner.generate_schedule()
                print("\n Schedule generated successfully.")

            case "2": 
                if planner: 
                    planner.display_schedule()
                    print("\nValidadtion Results: ")
                    if planner.validate_schedule():
                        print("Schedule is valid.")
                    else:
                        print("Schedule is invalid.")
                else: 
                    print("No schedule available. Please generate a schedule first");
                
            case "3":
                if planner:
                    filename = input("Enter CSV filaname (default: schedule.csv): ") or "schedule.csv"
                    planner.export_schedule_csv(filename)
                else:
                    print("No schedule available. Please generate a schedule first");
            
            case "4":
                if planner:
                    filename = input("Enter Excel filename (default: schedule.xlsx): ") or "schedule.xlsx"
                    planner.export_schedule_excel(filename)
                else:
                    print("No schedule available. Please generate one first.")

            case "5":
                if planner:
                    try: 
                        sid = int(input("Enter staff ID for leave: "))
                        day = int(input("Enter day number (1-based): ")) - 1
                        planner.handle_leave_request(sid, day)
                    except Exception as e:
                        print("Invalid input: ", e);
                else: 
                    print("No schedule available. Please generate a schedule first");
            
            case "0": 
                print("Exiting the program, goodbye!")
                sys.exit()
                
            case _:
                print("Invalid choice. Try again")


if __name__ == "__main__": 
    main()

            
        
        
    
