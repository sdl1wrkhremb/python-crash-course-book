class User:
    """a simple attempt to represent a user"""

    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.login_attempts = 0

    def describe_user(self):
        """print summary of user's information"""
        print(f"User: {self.first_name.title()} {self.last_name.title()}")
        print(f"\t Email: {self.email}")
        print(f"\t Phone: {self.phone}")

    def greet_user(self):
        """greet the user"""
        print(
            f"\nHello {self.first_name.title()} {self.last_name.title()}, hope you are enjoying coding with Python!")

    def increment_login_attempts(self):
        """increments a users number of login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """resets a users number of login attempts to 0"""
        self.login_attempts = 0


ryan = User('ryan', 'smith', 'ryan@aol.com', '999-888-7777')

ryan.describe_user()
ryan.greet_user()

ryan.increment_login_attempts()
ryan.increment_login_attempts()
ryan.increment_login_attempts()
ryan.increment_login_attempts()
ryan.increment_login_attempts()

print(f" {ryan.first_name} has attempted to login {ryan.login_attempts} times!")

ryan.reset_login_attempts()

print(f" {ryan.first_name} has attempted to login {ryan.login_attempts} times!")
