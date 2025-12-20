class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        print(f"Opening connection to {connection_string}")
        # Simulate resource allocation
        self.is_open = True

    def __del__(self):
        # Called when an object is about to be destroyed
        if self.is_open:
            print(f"Closing connection to {self.connection_string}")
            self.is_open = False


# Memory management in action
def process_data():
    db = DatabaseConnection("postgresql://localhost/mydb")
    # Use database...
    # When the function exits, db is destroyed and the connection closed


process_data()
# Output: Opening connection to postgresql://localhost/mydb
#         Closing connection to postgresql://localhost/mydb