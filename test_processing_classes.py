# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# Sonu Mishra, 6/10/2025, created script with help from ChatGPT
# Citation: OpenAI. (2025). ChatGPT (GPT-4o, June 12 2025 version) [Large language model]. https://chat.openai.com/
# ------------------------------------------------------------------------------------------------- #

import unittest
from unittest.mock import mock_open, patch
import json

# Import the classes you're testing
from processing_classes import FileProcessor
from data_classes import Employee

class TestFileProcessor(unittest.TestCase):

    def setUp(self):
        # Create a sample employee object list for writing tests
        self.mock_employee_list = [
            Employee("John", "Doe", "2020-01-01", 5),
            Employee("Jane", "Smith", "2021-05-15", 4)
        ]

        # Create a sample JSON string for reading tests
        self.mock_file_data = json.dumps([
            {
                "FirstName": "John",
                "LastName": "Doe",
                "ReviewDate": "2020-01-01",
                "ReviewRating": 5
            },
            {
                "FirstName": "Jane",
                "LastName": "Smith",
                "ReviewDate": "2021-05-15",
                "ReviewRating": 4
            }
        ])

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_read_file_not_found(self, mock_file):
        # Simulate file not found
        mock_file.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            FileProcessor.read_employee_data_from_file("testfile.json", [], Employee)

    @patch("builtins.open", new_callable=mock_open, read_data=None)
    def test_read_other_exception(self, mock_file):
        # Simulate non-specific error
        mock_file.side_effect = Exception
        with self.assertRaises(Exception):
            FileProcessor.read_employee_data_from_file("testfile.json", [], Employee)

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_read_file_success(self, mock_file):
        # Mock the file content
        mock_file.return_value.read.return_value = self.mock_file_data
        employee_list = []
        result = FileProcessor.read_employee_data_from_file("testfile.json", employee_list, Employee)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].first_name, "John")
        self.assertEqual(result[1].last_name, "Smith")
        self.assertEqual(result[0].review_rating, 5)

    @patch("json.dump")
    @patch("builtins.open", new_callable=mock_open)
    def test_write_file_success(self, mock_file, mock_json_dump):
        FileProcessor.write_employee_data_to_file("testfile.json", self.mock_employee_list)
        mock_file.assert_called_once_with("testfile.json", "w")
        mock_json_dump.assert_called_once()
        dumped_data = mock_json_dump.call_args[0][0]

        # Verify structure of written data
        self.assertEqual(dumped_data[0]["FirstName"], "John")
        self.assertEqual(dumped_data[0]["ReviewRating"], 5)

    def test_write_type_error(self):
        with self.assertRaises(Exception):
            FileProcessor.write_employee_data_to_file("testfile.json", ["invalid data object"])


if __name__ == '__main__':
    unittest.main()
