# 📘 Assignment: Working with Files in Python

## 🎯 Objective

Learn to read and write data to files, persist information between program runs, and work with common file formats like text and CSV. You'll build practical skills for saving user data and loading it back.

## 📝 Tasks

### 🛠️ Read and Write Text Files

#### Description

Create a program that reads text from a file and writes data to a file. This foundational skill allows your programs to persist information and work with existing data sources.

#### Requirements

Completed program should:

- Open a text file in read mode and display its contents
- Write text data to a new file in write mode
- Handle file paths correctly for different operating systems
- Close files properly (or use context managers)
- Demonstrate both reading an existing file and creating a new file

### 🛠️ Parse and Process CSV Data

#### Description

Work with comma-separated values (CSV) files to read structured data, process it, and write results back. CSV is a common format for data exchange between programs.

#### Requirements

Completed program should:

- Read data from a CSV file line by line
- Parse CSV rows into organized data (lists or dictionaries)
- Filter or transform the data based on conditions
- Write processed results to a new CSV file
- Handle headers and maintain data integrity

### 🛠️ Build a Simple Data Storage System (Stretch Goal)

#### Description

Create a program that saves and loads user data persistently. This could be a contact list, task manager, or similar application where data survives between program restarts.

#### Requirements

Completed program should:

- Save multiple records to a file (using JSON or CSV format)
- Load saved records back into the program on startup
- Allow users to add new records and save them
- Maintain data consistency between file and program memory
- Handle edge cases like missing files or corrupt data
