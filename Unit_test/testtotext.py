import unittest
from main import from_morse_code  # Replace 'your_module' with the actual module name


class TestFromMorseCode(unittest.TestCase):
    def test_from_morse_code_valid_input(self):
        morse_code = "... --- ..."
        result = from_morse_code(morse_code)
        self.assertEqual(result, "SOS")

    def test_from_morse_code_invalid_input(self):
        morse_code = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.. -!"
        result = from_morse_code(morse_code)
        self.assertEqual(result, "H E L L O   W O R L D !")

    def test_from_morse_code_empty_input(self):
        morse_code = ""
        result = from_morse_code(morse_code)
        self.assertEqual(result, "")

    def test_from_morse_code_unknown_morse_sequence(self):
        morse_code = "..--.."
        result = from_morse_code(morse_code)
        self.assertEqual(result, "Unknown")


if __name__ == '__main__':
    unittest.main()
