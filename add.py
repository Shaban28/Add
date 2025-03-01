from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Addition App! Use /add?num1=VALUE&num2=VALUE to add two numbers."

@app.route('/add')
def add():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        return f"The sum of {num1} and {num2} is {num1 + num2}"
    except ValueError:
        return "Invalid input! Please provide numeric values for num1 and num2."

if __name__ == "__main__":
    app.run(debug=True)
