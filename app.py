from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/api/clf", methods=["post"])
def clf():
  if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400

  print(request.json)
  body = request.json
  pulls = body["pulls"]

  results = []
  for pull in pulls:
    #   result = something(pull["body"])
      category = "WHY"
      results.append({"id": pull["id"], "category": category})

  return jsonify(results=results)