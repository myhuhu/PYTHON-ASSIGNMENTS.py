
class Employee:
    company_name = "TechSolutions Ltd"

    def __init__(self, name, position="Junior Developer"):
        self.name = name
        self.position = position

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Company: {self.company_name}")
        print("-" * 30)

# Creating employee objects
emp1 = Employee("Alice", "Project Manager")
emp2 = Employee("Bob")

# Displaying details
emp1.display_details()
emp2.display_details()
