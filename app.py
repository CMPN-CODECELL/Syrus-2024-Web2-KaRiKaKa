from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
import json

app = Flask(__name__, template_folder='templates', static_url_path='/static')

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel("gemini-pro")

conversation_history_file = "conversation_history.json"

def load_conversation_history():
    if os.path.exists(conversation_history_file):
        with open(conversation_history_file, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []

def save_conversation_history(history):
    with open(conversation_history_file, "w") as f:
        json.dump(history, f, indent=4)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/petPage')
def petPage():
    conversation_history = load_conversation_history()
    return render_template('petPage.html', conversation_history=conversation_history)

@app.route('/registerPage')
def registerPage():
    return render_template('registerPage.html')

@app.route('/loginPage')
def loginPage():
    return render_template('loginPage.html')

@app.route('/journal')
def journal():
    return render_template('journal.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/game2')
def game2():
    selected_game = request.args.get('selected_game')
    return render_template('game2.html', selected_game=selected_game)

@app.route('/fitness')
def fitness():
    return render_template('fitness.html')

@app.route('/exercise')
def exercise():
    selected_exercise = request.args.get('selected_exercise', '')
    return render_template('exercise.html', selected_exercise=selected_exercise)

@app.route('/process_input', methods=['POST'])
def process_input():
    data = request.get_json()
    user_input = data['inputText']

    # Load conversation history
    conversation_history = load_conversation_history()

    # Update the prompt with context
    prompt = "You are now an AI not integrated into a mental health and well-being website. You are going to act like the user's virtual pet. Your task is to listen to the user and then cheer them up according to their mood. Be their personal therapist and someone they can confide in. Give your response in html format. \n Conversation History: \n"
    for entry in conversation_history:
        prompt += f"- {entry['user']}: {entry['text']}\n"
    prompt += f"- User: {user_input}\n"

    # ... (Optional, modify this section if needed)

    response = model.generate_content(prompt)
    # if response.parts is not None:
    #     return response.parts[0].text
    # else:
    #     return "Unable to generate a response."

    # Update conversation history and save
    conversation_history.append({"user": user_input, "text": response.text})
    save_conversation_history(conversation_history)

    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
