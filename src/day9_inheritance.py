"""
day9_inheritance.py
Practicing inheritance, super(), overriding, and polymorphism.
Author: Viraj
"""


class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def describe(self) -> str:
        return f"{self.name} earns INR{self.salary}"


class Manager(Employee):
    def __init__(self, name: str, salary: int, team_size: int):
        # YOUR CODE: call super().__init__() to reuse Employee's setup
        super().__init__(name, salary)
        self.team_size = team_size
        # YOUR CODE: set self.team_size

    def describe(self) -> str:
        # YOUR CODE: call super().describe(), then add team size info
        base = super().describe()
        return f"{base}, managing a team of {self.team_size}"
        # e.g. "Viraj earns INR80000, managing a team of 5"
    


def main():
    people = [
        Employee("Alice", 50000),
        Manager("Viraj", 80000, 5),
        Employee("Bob", 45000),
    ]

    for person in people:
        print(person.describe())


if __name__ == "__main__":
    main()