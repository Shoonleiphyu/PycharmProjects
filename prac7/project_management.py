import csv
import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}" \
               f"completion: {self.completion_percentage}"

    def __lt__(self, other):
        return self.priority < other.priority

    def sort_project(self):
        return self.priority.sort()

    def date_format(self):
        return self.start_date == datetime.datetime.strptime(self.start_date, "%d/%m/%Y").date()


def load_projects():
    file_name = input("Enter a file name you want to load your projects from: ")
    if not file_name.endswith(".txt"):
        file_name += '.txt'
    all_projects = []
    file = open(file_name, 'r')
    next(file)
    reader = file.readlines()

    for line in reader:
        name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
        all_projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage)))
    file.close()
    return all_projects


def save_projects(projects):
    file_name = input("Enter a file name you want your projects to save to: ")
    if not file_name.endswith(".txt"):
        file_name += '.txt'
    file = open(file_name, 'w')
    file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
    for project in projects:
        file.write(f"{project.name}\t{project.start_date}\t{str(project.priority)}\t{str(project.cost_estimate)}"
                   f"\t{str(project.completion_percentage)}\n")
    file.close()


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    incomplete_projects.sort(key=lambda x: x.priority)
    completed_projects.sort(key=lambda x: x.priority)

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)

    print("Completed projects:")
    for project in completed_projects:
        print(project)


def filter_projects_by_date(projects):
    filtered_projects = []

    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    for p in projects:
        project_start_date = datetime.datetime.strptime(p.start_date, "%d/%m/%Y").date()
        if project_start_date > filter_date:
            filtered_projects.append(p)

    filtered_projects.sort(key=lambda x: x.start_date)
    for project in filtered_projects:
        print(project)


def add_new_project():
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")

    new_project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
    return new_project


def update_project(projects):
    for i in range(len(projects)):
        print(str(i), projects[i])

    project_index = int(input("Project choice: "))
    print(projects[project_index])
    new_percentage = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))

    projects[project_index].priority = new_priority
    projects[project_index].completion_percentage = new_percentage

    return projects