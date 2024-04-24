from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["survey_database"]
collection = db["user_data"]

# Route to render the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to process form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    # Get form data
    age = request.form['age']
    gender = request.form['gender']
    total_income = request.form['total_income']
    utilities_expense = request.form.get('utilities_expense', '')
    entertainment_expense = request.form.get('entertainment_expense', '')
    school_fees_expense = request.form.get('school_fees_expense', '')
    shopping_expense = request.form.get('shopping_expense', '')
    healthcare_expense = request.form.get('healthcare_expense', '')

    # Store data in MongoDB
    user_data = {
        'age': age,
        'gender': gender,
        'total_income': total_income,
        'expenses': {
            'utilities': utilities_expense,
            'entertainment': entertainment_expense,
            'school_fees': school_fees_expense,
            'shopping': shopping_expense,
            'healthcare': healthcare_expense
        }
    }
    collection.insert_one(user_data)

    # Redirect to success page after form submission
    return redirect(url_for('success'))

# Route to render the success page
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development





