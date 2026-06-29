from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# About Page
@app.route("/about")
def about():
    return render_template("about.html")


# Feedback Page
@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

# Model Page
@app.route("/model")
def model():
    return render_template("model.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/tc")
def tc():
    return render_template("tc.html")
# Voice Processing
@app.route("/process", methods=["POST"])
def process():

    data = request.get_json()

    text = data["text"]

    ################################################
    #              YOUR PYTHON CODE
    ################################################
    symptoms=['headache','fever','cough','fatigue','nausea','dizziness','sore throat','shortness of breath','chest pain','abdominal pain','diarrhea','vomiting','rash','joint pain','muscle aches','chills','sweating','loss of appetite','weight loss','insomnia','anxiety','depression']
    keywords = text.lower()
    sumps=[]
    for keyword in symptoms:
        if keyword in keywords:
            sumps.append(keyword)
    if len(sumps)>0:
        result = f"You said {text}, symptom detected: {', '.join(sumps)}. This could be a sign of cancer. Consider consulting a healthcare professional for further evaluation."
    else:
        result = "No symptoms detected."
    ################################################

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)