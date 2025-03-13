from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app) 

apikey = "gsk_fv8EZhAeFM0vyI6jJs44WGdyb3FYcI7vBQrqpNVgGAFQyWGM46"  # Replace with your actual API key

# Store conversation history
conversation_history = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global conversation_history

    data = request.get_json()
    user_message = data.get("message")

    if not user_message:
        return jsonify({"reply": "I didn't get that."})

    client = Groq(api_key=apikey)

    # Append user message to conversation history
    conversation_history.append({"role": "user", "content": user_message})

    chat_completion = client.chat.completions.create(
        messages=conversation_history,
        model="llama3-8b-8192",  # Change this if needed
    )

    bot_response = chat_completion.choices[0].message.content

    # Append bot response to conversation history
    conversation_history.append({"role": "assistant", "content": bot_response})

    return jsonify({"reply": bot_response})


if __name__ == "__main__":
    app.run(debug=True)
