from flask import Flask, render_template, request
import sys
import os

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import scripts
from scripts.magic8ball import get_fortune
from scripts.shipping import get_all_shipping_costs, find_cheapest_shipping_method

app = Flask(__name__)

# Define routes using original app.py code
@app.route('/')
def home():
    # home route code here
    return render_template('home.html')

# Magic 8 Ball route
@app.route('/magic8ball', methods=['GET', 'POST'])
def magic8ball():
    answer = None
    name = ""
    question = ""

    if request.method == 'POST':
        name = request.form.get('name', '')
        question = request.form.get('question', '')
        if question:
            answer = get_fortune(name, question)

    return render_template('magic8ball.html',
                           answer=answer,
                           name=name,
                           question=question)

# Shipping Calculator route
@app.route('/shipping', methods=['GET', 'POST'])
def shipping():
    shipping_costs = None
    cheapest_method = None
    cheapest_cost = None
    weight = None
    error = None

    if request.method == 'POST':
        try:
            weight = float(request.form.get('weight', 0))

            if weight <= 0:
                error = "Weight must be more than 0."
            else:
                shipping_costs = get_all_shipping_costs(weight)
                cheapest_method, cheapest_cost = find_cheapest_shipping_method(shipping_costs)
        except ValueError:
            error = "Please enter a valid weight."

    return render_template('shipping.html',
                           shipping_costs=shipping_costs,
                           cheapest_method=cheapest_method,
                           cheapest_cost=cheapest_cost,
                           weight=weight,
                           error=error)