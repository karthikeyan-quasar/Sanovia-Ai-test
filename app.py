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
def model(text='jgiu46FGHj798hb'):
    if text=='jgiu46FGHj798hb':
        return 'No symptoms detected'
    symptoms=['runny nose', 'sneezing', 'cough', 'sore throat','wheezing', 'shortness of breath', 'chest tightness','chills', 'high fever', 'profuse sweating', 'headache']
    user = text
    user_symp=[]
    for i in symptoms:
        if i in user:
            user_symp.append(i)
    disease = {'Common cold':['runny nose', 'sneezing', 'cough', 'sore throat'],
               'Asthma':['wheezing', 'shortness of breath', 'chest tightness'],
               'Malaria':['chills', 'high fever', 'profuse sweating', 'headache']}
    score ={'Common cold':0,
            'Asthma':0,
            'Malaria':0}
    keys=list(disease)
    for i in keys:
        samp_dis=disease[i]
        count = 0
        for j in samp_dis:
            if j in user_symp:
                count+=1
        score[i]=count/len(user_symp)
    max_score=0
    index = []
    for i in keys:
        if score[i]>max_score:
            max_score = score[i]
    for i in keys:
        if score[i]==max_score:
            index.append(i)
    disease_detected = index[0]
    cure={'Common cold':'No cure; symptom relief (rest, fluids, decongestants)',
          'Asthma':'Managed with rescue inhalers (albuterol) and steroids',
          'Malaria':'Cured with antimalarial drugs (Artemisinin-based)'}
    return 'You said: '+text+' Disease detected: '+disease_detected+'cure: '+cure[disease_detected]
# Voice Processing
@app.route("/process", methods=["POST"])
def process():

    data = request.get_json()

    text = data["text"]

    text = text.lower()
    result = model(text)

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)