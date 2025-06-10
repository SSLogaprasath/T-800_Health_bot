from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__, static_folder='static')

# Configuration
TOGETHER_API_KEY = "tgp_v1_e-BNLgJeZcy9178USJGmuGmT-WZsjfhVTjjLI2D93G8"  # 🔐 Replace with your actual key
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"

# Serve the frontend
@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'index.html')

# Chat API endpoint
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        messages = data.get('messages', [])
        
        payload = {
            "model": MODEL_NAME,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 800
        }

        headers = {
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            "https://api.together.xyz/v1/chat/completions",
            json=payload,
            headers=headers
        )
        response.raise_for_status()
        
        ai_message = response.json()["choices"][0]["message"]["content"]
        return jsonify({"response": ai_message})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)