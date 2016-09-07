from flask import Flask
from flask import render_template
from flask import request

import phone_parser

app = Flask(__name__)


def validate_text(text):
    """
    Simple function to validate the text input
    :param text: input from the form to ensure is appropriate size
    :return: error string
    """
    error = None
    text = text.strip()
    if len(text) < 10:
        error = "Text is too short must be greater than 10 characters"
    elif len(text) > 1000:
        error = "Text is too long must be less than 1000 characters"

    return error


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main page will process returning just the form as well as the POST method
    to return either extracted numbers or errors
    :return: rendered template
    """

    if request.method == 'POST':
        text_body = request.form['data']

        error = validate_text(text_body)
        if error:
            return render_template("index.html", error=error)

        number_tuples = phone_parser.parse_text(text_body)
        numbers = phone_parser.format_numbers(number_tuples)

        return render_template("index.html", numbers=numbers)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run()
