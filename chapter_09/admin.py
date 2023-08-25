from users import User
from privileges import Privileges


class Admin(User):
    """a simple attempt to represent a user"""

    def __init__(self, first_name, last_name, username, email, phone):
        """initialize admin user"""
        super().__init__(first_name, last_name, username, email, phone)
        self.privileges = Privileges()


admin1 = Admin('ryan', 'smith', 'admin1', 'admin1@company.com', '999-888-7777')
admin1.describe_user()

admin1.privileges.show_privileges()

admin1_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]

admin1.privileges.privileges = admin1_privileges

print(admin1.privileges.privileges)


admin2 = Admin('james', 'smith', 'admin2',
               'admin2@company.com', '999-888-7777')

admin2.privileges.show_privileges()
