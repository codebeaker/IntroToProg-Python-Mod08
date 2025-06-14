# IntroToProg-Python-Mod08: Assignment 8, Employee Ratings README

# Introduction
In this document we describe a simple python CLI-based application that allows users to enter ratings and review dates about employees (along with employee first name and last name), see saved and unsaved data, and save data to a json file. 
# User input and data structures
Users navigate through the program through a MENU that is a constant string. When users indicate that they want to enter information about an employee, they are prompted through python’s input() function to enter the employee’s first and last name, review date, and rating. Error handling prevents numbers in names, invalid date formats, and ratings outside of {1, 2, 3, 4 5}. 
Data is ultimately stored in a json file. When the program is first loaded, the existing data is read in and transformed to a list of employee objects, defined in the Employee class in the data_classes.py file. This class inherits first and last name properties from the Person class in the same file, and adds more for review date and ratings. When users enter information about an employee, this information is stored as an employee object. On saving, the list of unsaved objects is appended to the list of saved objects, and the full list of saved objects is written back to the json file. 
# Application structure 
The application is designed to be relatively modular. The main.py file calls the others. The data_classes.py contains the definitions of key objects, constants, and variables; the processing_classes.py contains classes grouping functions about reading and writing of data; and the presentation_classes.py contains much of the core of the application, the functions related to how user input is managed within the application. 
#import libraries and frameworks
import json
import io as _io
from datetime import date
import unittest

#import application modules
import data_classes as data
import processing_classes as proc
import presentation_classes as pres
import test_data_classes as test_data
import test_presentation_classes as test_pres


# Beginning of the main body of this script
employees = proc.FileProcessor.read_employee_data_from_file(file_name=data.FILE_NAME,
                                                       employee_data=data.employees_saved,
                                                       employee_type=data.Employee)  # Note this is the class name (ignore the warning)


**Figure 1: The beginning of main.py, pulling everything together through import statements and references like “proc.FileProcessor”**

# Unit Tests Ex Machina
Along with the application we include unit tests to verify that each chunk of code is running. While I was able to write the data_classes unit tests myself, I actually turned to ChatGPT for help for the unit tests for the processing and presentation classes (it is cited in the changelog at the top for the relevant files). In the case of the former, it was because I wasn’t sure how to write unit tests for reading and writing data. However, going through the code I can see that it works by creating sample object strings and json strings to feed to the functions. The code includes a few other things whose purpose I had to look up. The decorator “@patch” turns out to mock an object for your test so you don’t have to call it from another file. “builtins.open” means that you are not actually opening and writing to real files during your unit test. “new_callable=mock_open” simulates file objects. 

@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_file_not_found(self, mock_file):
    # Simulate file not found
    mock_file.side_effect = FileNotFoundError
    with self.assertRaises(FileNotFoundError):
        FileProcessor.read_employee_data_from_file("testfile.json", [], Employee)
**Figure 2: Snippet of Chat-GPT created unit tests for the test_processing_classes.py file illustrating some of the code that is new to me.**
This was by far the most I have used Chat GPT in this course. It does have a reputation for being really good at writing unit tests and I suppose it delivered in this instance. Still, I don’t intend to be dependent on bots for writing code, so learning to write these portions independently will be future work. 

# Summary
This simple CLI application allows users to enter information about employees including first and last name, review date, and rating 1-5. It is accompanied by unit tests to make sure each chunk of code runs. Chat GPT was in this case instrumental in helping write unit tests. 
![image](https://github.com/user-attachments/assets/97166fb2-2e7f-4870-8b57-dfd6c551cc24)
