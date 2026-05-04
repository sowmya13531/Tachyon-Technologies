from storage import load_data, save_data
from manager import StudentManager

def main():
    data = load_data()
    manager = StudentManager(data)

    while True:
        print("\n1. Add Student")
        print("2. View All")
        print("3. Find Topper")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.show_all()
        elif choice == "3":
            manager.find_topper()
        elif choice == "4":
            manager.update_student()
        elif choice == "5":
            manager.delete_student()
        elif choice == "6":
            save_data(manager.to_list())
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()