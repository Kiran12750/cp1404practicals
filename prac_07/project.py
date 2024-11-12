"""
Time Estimate: 6 hours

This project management system allows users to load, save, display, filter, add, and update projects.
The program handles project data with a Project class and supports various user actions.
"""
import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        # Format the project details as a string
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def is_completed(self):
        return self.completion_percentage == 100

    @staticmethod
    def compare_by_priority(project):
        return project.priority

    def update(self, new_percentage=None, new_priority=None):
        if new_percentage is not None:
            self.completion_percentage = int(new_percentage)
        if new_priority is not None:
            self.priority = int(new_priority)
