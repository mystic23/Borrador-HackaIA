from flask import Flask, jsonify, render_template, request, session
import google.generativeai as genai
from api import Gemini_API_KEY as api
from google.cloud import firestore
import os
import json

# Configura el acceso a Google Cloud
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'GanaderIAKey.json'
db = firestore.Client()

genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

app = Flask(__name__)

chat_history = []

@app.route('/')
def index():
    return render_template('chat.html', chat_history=chat_history)

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    try:
        user_input = request.json.get('user_input')
        if user_input:
            # Consulta la base de datos basada en el input del usuario
            doc_ref = db.collection('ganaderia').document(user_input)
            doc = doc_ref.get()
            if doc.exists:
                db_info = doc.to_dict()
                context = json.dumps(db_info)
            else:
                context = "No information found in the database."

            # Envía el contexto a la API de Generative AI
            response = chat.send_message(user_input + " Context: " + context)
            chat_history.append({"user": user_input, "bot": response.text})
            return jsonify({"response": response.text})
        else:
            return jsonify({"error": "No user input provided."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
