"""
File I/O and Data Persistence Starter Code

This file provides a framework for working with files in Python.
Complete the tasks by implementing reading, writing, and parsing file operations.
"""

import csv


# ===== TASK 1: Read and Write Text Files =====

def read_text_file(filename):
    """
    TODO: Implement this function to read and return the contents of a text file.
    Hint: Use the open() function with 'r' mode, or use a context manager (with statement)
    """
    pass


def write_text_file(filename, content):
    """
    TODO: Implement this function to write content to a text file.
    Hint: Use open() with 'w' mode. Be careful: 'w' mode overwrites existing files!
    """
    pass


# ===== TASK 2: Parse and Process CSV Data =====

def read_csv_file(filename):
    """
    TODO: Implement this function to read a CSV file and return the data as a list of dictionaries.
    Hint: Use the csv module's DictReader to preserve column names
    """
    pass


def write_csv_file(filename, fieldnames, rows):
    """
    TODO: Implement this function to write data to a CSV file.
    Args:
        filename: The output file path
        fieldnames: List of column names (e.g., ['name', 'age', 'email'])
        rows: List of dictionaries, one per row
    Hint: Use csv.DictWriter() to write structured data
    """
    pass


# ===== TASK 3: Data Storage System (Stretch Goal) =====

class SimpleDataStore:
    """
    TODO: Implement a simple data storage system that can save and load records from a file.
    
    This class should:
    - Load existing data from a file on initialization
    - Provide methods to add new records
    - Save all records to a file
    - Handle missing files gracefully
    """
    
    def __init__(self, filename):
        """Initialize the data store with a filename."""
        pass
    
    def load(self):
        """Load records from the file. Create an empty list if file doesn't exist."""
        pass
    
    def add_record(self, record):
        """Add a new record to the data store."""
        pass
    
    def save(self):
        """Save all records to the file."""
        pass
    
    def get_all_records(self):
        """Return all stored records."""
        pass


# Example usage (uncomment to test):
# if __name__ == "__main__":
#     # Task 1: Text files
#     write_text_file("example.txt", "Hello, File I/O!")
#     content = read_text_file("example.txt")
#     print(content)
#
#     # Task 3: Data store
#     store = SimpleDataStore("contacts.json")
#     store.add_record({"name": "Alice", "email": "alice@example.com"})
#     store.save()
#     print(store.get_all_records())
