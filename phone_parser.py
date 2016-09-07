import re

REGEX = r'\(?(\d{3})\)?[\s\.\-]*(\d{3})[\s\.\-]*(\d{4})'


def parse_text(text):
    """
    Takes a string and returns a list of matching numbers
    :param text: string of input to find and parse numbers from
    :return: list of tuples with phone number pieces
    """

    matches = re.findall(REGEX, text)
    return matches


def format_numbers(number_tuples):
    """
    Takes in a list of phone number tuples and formats them as (###) ###-####
    :param number_tuples: list of tuples containing the 3 parts of a number
    :return: List of formatted phone number string
    """
    format_string = "({0}) {1}-{2}"
    result = []

    for number in number_tuples:
        result.append(format_string.format(*number))

    return result
