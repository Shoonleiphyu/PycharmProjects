import project_management

filename = "projects.txt"
def main():
    MENU = """L- Load projects  
S- Save projects  
D- Display projects  
F- Filter projects by date
A- Add new project  
U- Update project
Q- Quit"""
    print(MENU)

    choice = input(">>> ").lower()

    current_projects = []

    while choice != 'q':
        if choice == 'l':
            current_projects = project_management.load_projects()
        elif choice == 's':
            if len(current_projects) < 1:
                print("Currently No Projects Loaded!")
            else:
                project_management.save_projects(current_projects)
        elif choice == 'd':
            if len(current_projects) < 1:
                print("Currently No Projects Loaded!")
            else:
                project_management.display_projects(current_projects)
        elif choice == 'f':
            if len(current_projects) < 1:
                print("Currently No Projects Loaded!")
            else:
                project_management.filter_projects_by_date(current_projects)
        elif choice == 'a':
            if len(current_projects) < 1:
                print("Currently No Projects Loaded!")
            else:
                current_projects.append(project_management.add_new_project())
        elif choice == 'u':
            if len(current_projects) < 1:
                print("Currently No Projects Loaded!")
            else:
                current_projects = project_management.update_project(current_projects)
        else:
            print("Invalid menu option. Enter your choice again: ")
        print(MENU)
        choice = input(">>> ").lower()
    print("Thank you for using custom-built project management software.")


main()
