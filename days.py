from flask import Flask, request, jsonify

app = Flask(__name__)

def daysmsg(day):
    if day.lower() in ['monday', 'tuesday', 'thursday', 'friday']:
        return "Oh, it's a weekday"
    elif day.lower() == 'wednesday':
        return "Happy Hump Day!"
    elif day.lower() in ['saturday','sunday']:
        return "Its weekend "
    else:
        return "Whoop Whoop!"

def travel_eligibility(age):
    if age <= 18:
        return "You are not eligible to travel."
    elif 19 <= age <= 30:
        return "You are eligible for budget travel with a cost of 100€."
    else:
        return "You are eligible for regular travel with a cost of 200€."

@app.route('/check_day', methods=['POST'])
def check_day():
    data = request.get_json()
    day = data['day'] 
    return jsonify({'message': day})

@app.route('/check_eligibility', methods=['POST'])
def check_eligibility():
    data = request.get_json()
    age = int(data['age']) 
    return jsonify({'message': 'Response for check_eligibility'})

if __name__ == '__main__':
    app.run(debug=True)
