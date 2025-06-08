import random

def main_menu():
    print("\n=== Pool Consultant Management System ===")
    print("1. Resume Agent")
    print("2. Opportunity Agent")
    print("3. Attendance Agent")
    print("4. Training Agent")
    print("5. Exit")
    choice = input("Select an option (1-5): ")
    return choice

def resume_agent():
    print("\n--- Resume Agent ---")
    print("1. View Resume")
    print("2. Update Resume")
    print("3. Generate Tailored Resume")
    choice = input("Select an option (1-3): ")
    if choice == "1":
        print("Displaying your current resume...")
        print("Name: John Doe\nSkills: Python, AI, Data Analysis\nExperience: 5 years")
    elif choice == "2":
        print("Updating your resume...")
        print("Enter new skill to add: ")
        new_skill = input()
        print(f"Skill '{new_skill}' added to your resume!")
    elif choice == "3":
        print("Generating tailored resume for a specific opportunity...")
        print("Resume optimized with relevant keywords for the selected job.")
    else:
        print("Invalid choice. Returning to main menu.")

def opportunity_agent():
    print("\n--- Opportunity Agent ---")
    print("1. View Available Opportunities")
    print("2. Match Opportunities to Your Profile")
    choice = input("Select an option (1-2): ")
    if choice == "1":
        print("Fetching available opportunities...")
        print("1. Data Scientist at XYZ Corp\n2. AI Engineer at ABC Ltd\n3. Python Developer at DEF Inc")
    elif choice == "2":
        print("Matching opportunities to your profile...")
        matched_opportunity = random.choice(["Data Scientist at XYZ Corp", "AI Engineer at ABC Ltd", "Python Developer at DEF Inc"])
        print(f"Best match for you: {matched_opportunity}")
    else:
        print("Invalid choice. Returning to main menu.")

def attendance_agent():
    print("\n--- Attendance Agent ---")
    print("1. View Attendance Record")
    print("2. Log Attendance")
    choice = input("Select an option (1-2): ")
    if choice == "1":
        print("Fetching attendance record...")
        print("Attendance: 95% | Absences: 2 days | Late Logins: 1 day")
    elif choice == "2":
        print("Logging attendance for today...")
        print("Attendance logged successfully!")
    else:
        print("Invalid choice. Returning to main menu.")

def training_agent():
    print("\n--- Training Agent ---")
    print("1. View Recommended Trainings")
    print("2. Track Training Progress")
    choice = input("Select an option (1-2): ")
    if choice == "1":
        print("Fetching recommended trainings...")
        print("1. Advanced Python Programming\n2. Machine Learning Basics\n3. Data Visualization with Tableau")
    elif choice == "2":
        print("Fetching training progress...")
        print("Completed: 2/5 trainings | In Progress: Machine Learning Basics")
    else:
        print("Invalid choice. Returning to main menu.")

def main():
    while True:
        choice = main_menu()
        if choice == "1":
            resume_agent()
        elif choice == "2":
            opportunity_agent()
        elif choice == "3":
            attendance_agent()
        elif choice == "4":
            training_agent()
        elif choice == "5":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
