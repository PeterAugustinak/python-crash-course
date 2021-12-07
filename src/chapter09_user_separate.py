class User:
    """Base class for modeling users"""

    def __init__(self, first_name, last_name, age, status, active=True):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.status = status
        self.active = active
        self.logging_attempts = 1

    def increment_login_attempts(self):
        self.logging_attempts += 1

    def reset_login_attempts(self):
        self.logging_attempts = 0

    def describe_user(self):
        print("User information: ")
        print(f"\t- {self.first_name}")
        print(f"\t- {self.last_name}")
        print(f"\t- {self.age}")
        print(f"\t- {self.status}")
        print(f"\t- {self.active}")

    def greet_user(self):
        print(f"Hello my dear {self.first_name}! How are you today?")
