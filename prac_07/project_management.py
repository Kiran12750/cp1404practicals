"""
Time Estimate: 6 hours

This project management system allows users to load, save, display, filter, add, and update projects.
The program handles project data with a Project class and supports various user actions.
"""
import os
import datetime
from project import Project


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return projects

    with open(filename, 'r') as file:
        lines = file.readlines()[1:]  # Skip the header line
        for line in lines:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    print(f"Loaded {len(projects)} projects from {filename}.")
    return projects


def save_projects(projects, filename):
    """Save the current list of projects to a file."""
    with open(filename, 'w') as file:
        # Write the header
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"Saved {len(projects)} projects to {filename}.")


def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_completed()], key=Project.compare_by_priority)
    completed = sorted([p for p in projects if p.is_completed()], key=Project.compare_by_priority)

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects, date_str):
    """Filter and display projects that start after a given date."""
    filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if p.start_date > filter_date]
    filtered_projects.sort(key=lambda p: p.start_date)

    for project in filtered_projects:
        print(f"{project}")


def add_new_project(projects):
    """Add a new project to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")

    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)
    print(f"Added new project: {project}")


def update_project(projects):
    """Update an existing project's percentage complete and/or priority."""
    print("Choose a project to update:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    print(f"Updating {project}")

    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")

    project.update(new_percentage if new_percentage else None, new_priority if new_priority else None)
    print(f"Updated project: {project}")


def main():
    projects = load_projects("projects.txt")

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save to: ")
            save_projects(projects, filename)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yy): ")
            filter_projects_by_date(projects, date_str)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Do you want to save before quitting? (y/n): ")
            if save_choice.lower() == 'y':
                filename = input("Enter filename to save to: ")
                save_projects(projects, filename)
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
