import unittest
from main import to_morse_code


class TestToMorseCode(unittest.TestCase):
    def test_to_morse_code_valid_characters(self):
        message = "HELLO"
        result = to_morse_code(message)
        self.assertEqual(result, ".... . .-.. .-.. --- ")

    def test_to_morse_code_invalid_characters(self):
        message = "#"
        result = to_morse_code(message)
        self.assertEqual(result, "This character # is not exist in morse!")

    def test_to_morse_code_empty_string(self):
        message = ""
        result = to_morse_code(message)
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
