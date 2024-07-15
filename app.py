# app.py

from flask import Flask, render_template, request
from src.factorial import Factorial  # Import the Factorial class from src.factorial
# from folder.file import class name

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            num = int(request.form['number'])
            fact = Factorial(num)
            result = fact.calculate()
        except ValueError:
            result = "Please enter a valid integer"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=False)
