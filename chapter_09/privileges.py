class Privileges():
    """a simple attempt to represent privileges for an admin user"""

    def __init__(self, privileges=[]):
        """initialize privileges"""
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")
