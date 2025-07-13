class Employee:
    """
    Base class representing an employee.
    """
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_payroll(self):
        """
        Abstract method to calculate the payroll for the employee.
        Must be implemented by derived classes.
        """
        raise NotImplementedError("Subclasses must implement calculate_payroll()")


class SalaryEmployee(Employee):
    """
    Derived class representing an employee paid a fixed weekly salary.
    """
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        """
        Calculate the payroll for a SalaryEmployee.
        """
        return self.weekly_salary


class HourlyEmployee(Employee):
    """
    Derived class representing an employee paid based on hours worked and hourly rate.
    """
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        """
        Calculate the payroll for an HourlyEmployee.
        """
        return self.hours_worked * self.hourly_rate


class CommissionEmployee(SalaryEmployee):
    """
    Derived class representing an employee paid a fixed weekly salary plus commission.
    Inherits from SalaryEmployee.
    """
    def __init__(self, emp_id, name, weekly_salary, commission):
        super().__init__(emp_id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        """
        Calculate the payroll for a CommissionEmployee.
        """
        return super().calculate_payroll() + self.commission


# Example usage
if __name__ == "__main__":
    # Create instances of different employee types
    salary_employee = SalaryEmployee(emp_id=101, name="Alice", weekly_salary=150)
