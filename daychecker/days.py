from flask import Flask, request, jsonify, render_template

app = Flask(__name__,static_url_path='/static', static_folder='static')

@app.route('/days.html', methods=["GET", "POST"])
def days_page():
    if request.method == "GET":
        
        return render_template('days.html')
    elif request.method == "POST":
      
        data = request.get_json()
        if not data or 'day' not in data:
            return jsonify({'error': 'Day parameter is missing.'}), 400
        day = data['day'] 
        message = daysmsg(day)
        return jsonify({'message': message})

def daysmsg(day):
    if day.lower() in ['monday', 'tuesday', 'thursday', 'friday']:
        return "Oh, it's a weekday"
    elif day.lower() == 'wednesday':
        return "Happy Hump Day!"
    elif day.lower() in ['saturday', 'sunday']:
        return "It's weekend"
    else:
        return "Whoop Whoop!"

@app.route('/check_eligibility', methods=['POST'])
def check_eligibility():
    data = request.get_json()
    if not data or 'age' not in data:
        return jsonify({'error': 'Age parameter is missing.'}), 400
    age = data['age']
    try:
        age = int(age)
    except ValueError:
        return jsonify({'error': 'Age must be a valid integer.'}), 400
    message = travel_eligibility(age)
    return jsonify({'message': message})

def travel_eligibility(age):
    if age <= 18:
        return "You are not eligible to travel."
    elif 19 <= age <= 30:
        return "You are eligible for budget travel with a cost of 100€."
    else:
        return "You are eligible for regular travel with a cost of 200€."

if __name__ == '__main__':
    app.run(debug=True)
