# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# Sonu Mishra, 6/10/2025, created script with help from ChatGPT
# Citation: OpenAI. (2025). ChatGPT (GPT-4o, June 12 2025 version) [Large language model]. https://chat.openai.com/
# ------------------------------------------------------------------------------------------------- #

import unittest

# import the relevant class
from data_classes import Person
from data_classes import Employee

# Testing Person Class--------------

class TestPerson(unittest.TestCase):
    def test_person_init(self): #Tests the constructor
        person = Person("John","Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    def test_person_invalid_name(self): #Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123","Doe")
        with self.assertRaises(ValueError):
            person = Person("John", "123")

    def test_person_str(self): #Tests the __str__() magic method
        person = Person("John","Doe")
        self.assertEqual(str(person), "John,Doe")

#Testing Employee Class
class TestEmployee(unittest.TestCase):

    def test_employee_init(self): #Tests the constructor
        employee = Employee("Marshall","Ericson",
                            "2000-01-03",5)
        self.assertEqual(employee.first_name, "Marshall")
        self.assertEqual(employee.last_name, "Ericson")
        self.assertEqual(employee.review_date, "2000-01-03")
        self.assertEqual(employee.review_rating,5)

    def test_employee_date_type(self): #Test the review date validation
        with self.assertRaises(ValueError):
            employee = Employee("Marshall","Ericson",
                                "invalid review date",5)

    def test_employee_rating_type(self): #Test the rating validation
        with self.assertRaises(ValueError):
            employee = Employee("Marshall","Ericson",
                                "2000-01-03",9.0)





if __name__ == '__main__':
    unittest.main()

