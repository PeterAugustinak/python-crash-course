from chapter09_user_separate import User


class Admin(User):
    """Inheritance class from User for modeling specific Admin user"""

    def __init__(self, first_name, last_name, age, status, active=True):
        super().__init__(first_name, last_name, age, status, active=True)
        self.privileges = Privileges()


class Privileges:
    """Class for operation with privileges"""

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Administrator's privileges: ")
        for privilege in self.privileges:
            print(f"\t- {privilege}")
