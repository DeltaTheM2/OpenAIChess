from flask import Flask, jsonify, request
from flask_cors import CORS  # Import the CORS package
from openai import OpenAI
import os
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# OpenAI API key
OpenaiApiKey = os.environ.get('OpenaiApiKey')
client = OpenAI(api_key=OpenaiApiKey)

@app.route("/query/<query>")
def respondToQuery(query):
  model_engine = "text-davinci-003"
  prompt = (f"{query}")

  completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[{
          "role": "user",
          "content": query
      }])

  return jsonify(completion.choices[0].message.content)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
