from flask import Flask, jsonify, request
from flask_cors import CORS  # Import the CORS package
import openai

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# OpenAI API key
OpenaiApiKey = os.environ.get('OpenaiApiKey')
openai.api_key = OpenaiApiKey


@app.route("/query/<query>")
def respondToQuery(query):
  model_engine = "text-davinci-003"
  prompt = (f"{query}")

  completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )

  message = completions.choices[0].text
  response = message.strip()
  return jsonify(response)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
