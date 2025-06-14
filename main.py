# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Sonu Mishra, 6/10/2025, edited script
# ------------------------------------------------------------------------------------------------- #

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

# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=data.MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            pres.IO.output_employee_data(data.employees_saved, data.employees_unsaved)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue


    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = pres.IO.input_employee_data(data.employees_unsaved, data.Employee)  # Note this is the class name (ignore the warning)
            pres.IO.output_employee_data(data.employees_saved, data.employees_unsaved)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            #move unsaved data to saved data
            pres.IO.move_unsaved_to_saved(data.employees_unsaved, data.employees_saved)
            #write the saved data to file
            proc.FileProcessor.write_employee_data_to_file(file_name=data.FILE_NAME, employee_data=data.employees_saved)
            #show the user what happened
            print(f"This data has now been saved to the {data.FILE_NAME} file:")
            pres.IO.output_employee_data(data.employees_saved, data.employees_unsaved)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
