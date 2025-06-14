# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# Sonu Mishra, 6/10/2025, created script
# ------------------------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch, call
from data_classes import Employee
from presentation_classes import IO

class TestIO(unittest.TestCase):

    @patch("builtins.print")
    def test_output_error_messages_without_exception(self, mock_print):
        IO.output_error_messages("Simple error message")
        mock_print.assert_called_with("Simple error message", end="\n\n")

    @patch("builtins.print")
    def test_output_error_messages_with_exception(self, mock_print):
        e = ValueError("Test error")
        calls = [
            call("Error occurred", end="\n\n"),
            call("-- Technical Error Message -- "),
            call(e, e.__doc__, type(e), sep='\n')
        ]
        IO.output_error_messages("Error occurred", e)
        mock_print.assert_has_calls(calls)

    @patch("builtins.print")
    def test_output_menu(self, mock_print):
        IO.output_menu("Menu goes here")
        calls = [
            call(),
            call("Menu goes here"),
            call()
        ]
        mock_print.assert_has_calls(calls)

    @patch("builtins.input", return_value="2")
    def test_input_menu_choice_valid(self, mock_input):
        choice = IO.input_menu_choice()
        self.assertEqual(choice, "2")

    @patch("presentation_classes.IO.output_error_messages")
    @patch("builtins.input", return_value="9")
    def test_input_menu_choice_invalid(self, mock_input, mock_error):
        choice = IO.input_menu_choice()
        mock_error.assert_called()
        self.assertEqual(choice, "9")

    @patch("builtins.print")
    def test_output_employee_data(self, mock_print):
        emp1 = Employee("John", "Doe", "2023-01-01", 5)
        emp2 = Employee("Jane", "Smith", "2023-01-01", 3)
        saved = [emp1]
        unsaved = [emp2]
        IO.output_employee_data(saved, unsaved)
        self.assertTrue(mock_print.called)

    @patch("builtins.input", side_effect=["John", "Doe", "2023-01-01", "5"])
    def test_input_employee_data_valid(self, mock_input):
        employee_data = []
        result = IO.input_employee_data(employee_data, Employee)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].first_name, "John")
        self.assertEqual(result[0].last_name, "Doe")
        self.assertEqual(result[0].review_date, "2023-01-01")
        self.assertEqual(result[0].review_rating, 5)

    def test_move_unsaved_to_saved(self):
        saved = []
        unsaved = [
            Employee("John", "Doe", "2023-01-01", 5),
            Employee("Jane", "Smith", "2023-01-01", 3)
        ]
        IO.move_unsaved_to_saved(unsaved, saved)
        self.assertEqual(len(saved), 2)
        self.assertEqual(len(unsaved), 0)


if __name__ == '__main__':
    unittest.main()

