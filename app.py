from flask import Flask, jsonify, request
from flask_cors import CORS  # Import the CORS package
import openai
import os
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# OpenAI API key
OpenaiApiKey = os.environ.get('OpenaiApiKey')
openai.api_key = OpenaiApiKey


@app.route("/query/<query>")
def respondToQuery(query):
  model_engine = "text-davinci-003"
  prompt = (f"{query}")

  completion = client.chat.completions.create(
      model="gpt-3.5-turbo-0125",
      messages=[{
          "role":
          "system",
          "content":
          "You are a helpful assistant designed to output JSON.",
      }, {
          "role": "user",
          "content": sentence
      }])

  message = completions.choices[0].text
  response = message.strip()
  return jsonify(response)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
