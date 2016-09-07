from unittest import TestCase
from phone_parser import parse_text, format_numbers


class TestPhoneParsing(TestCase):

    number = ("702", "555", "1212")
    second_number = ("702", "555", "1213")
    third_number = ("702", "555", "1214")

    def format_and_assert(self, format_string):
        """
        Simple function to take a format and test that the parse_text works
        :param format_string: formatted string
        """
        result = parse_text(format_string.format(*self.number))

        self.assertEqual(self.number, result[0],
                         msg="Parser returned incorrect result for formatter")

    def test_simple_phone(self):
        """ Tests (555) 555-1212 """
        self.format_and_assert("({0}) {1}-{2}")

    def test_dot_phone(self):
        """ Tests 333.333.3333 """
        self.format_and_assert("{0}.{1}.{2}")

    def test_no_spaces(self):
        """ Tests 5555551212"""
        self.format_and_assert("{0}{1}{2}")

    def test_country_code(self):
        """ Tests +1 555.555.1212"""
        self.format_and_assert("+1 {0}.{1}.{2}")

    def test_parentheses_extra_space(self):
        """ Tests Extra spaces (555)  555  -  55555 """
        self.format_and_assert("({0})  {1}  -  {2}")

    def test_text_with_multiple_numbers(self):
        """
        Tests a full text block with different number formats.
        """

        text_block = """This is the test of some phone numbers:
            (850) 555 - 1212
            (850)  555  -  1213
            8505551214
            850.555.1215
            +1 850.555.1216
            So many numbers to find (850)5551217
        """

        numbers = parse_text(text_block)

        self.assertEqual(len(numbers), 6, msg="Parser found incorrect number")
        self.assertEqual(("850", "555", "1212"), numbers[0],
                         msg="First number is incorrect")
        self.assertEqual(("850", "555", "1217"), numbers[5],
                         msg="Last number is incorrect")

    def test_format_numbers(self):
        """
        Tests the number formatter to ensure it is formatting and
        returning correctly
        """

        text_block = "8505551214 850.555.1215"

        number_tuples = parse_text(text_block)
        numbers = format_numbers(number_tuples)

        self.assertEqual(2, len(number_tuples),
                         msg="Formatter returned incorrect number of numbers")
        self.assertEqual("(850) 555-1214", numbers[0],
                         msg="First phone number incorrectly formatted")
        self.assertEqual("(850) 555-1215", numbers[1],
                         msg="Second phone number incorrectly formatted")

    def test_formatter_empty_list(self):
        """
        Test the instance where there are no numbers in the list and ensure
        no errors occur.
        """
        number_tuples = parse_text("")
        numbers = format_numbers(number_tuples)

        self.assertEquals(0, len(numbers))
