from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__, template_folder='templates')

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel("gemini-pro")

@app.route('/')
def index():
    print("working index.html")
    return render_template('petPage.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    data = request.get_json()
    input_text = data['inputText']

    # Call your backend Python function to get the response
    response_text = get_query(input_text)

    return jsonify({'response': response_text})

def get_query(query):
    # Update the prompt without specifying the animal
    prompt = "You are now an AI not integrated into a mental health and well-being website. You are going to act like the user's virtual pet. Your task is to listen to the user and then cheer them up according to their mood. Be their personal therapist and someone they can confide in.Give your response in html format. The user says the following:{}".format(query)
    print("Working")
    response = model.generate_content(prompt)
    # if response.parts is not None:
    #     return response.parts[0].text
    # else:
    #     return "Unable to generate a response."
    return response.text

if __name__ == '__main__':
    app.run(debug=True, port=3000)
