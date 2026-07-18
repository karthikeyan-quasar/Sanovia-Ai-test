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
def model(text):
    symptoms = [
    "running nose",
    "watery nose",
    "sneezing",
    "sneeze",
    "nose dripping",
    "throat pain",
    "pain when swallowing",
    "cough",
    "coughing",
    "red throat",
    "fever",
    "warm body",
    "mild fever",
    "hot body",
    "body pain",
    "body ache",
    "body breaking",
    "tired",
    "no strength",
    "weakness",
    "fast heart",
    "heart beating fast",
    "heart racing",
    "dry cough",
    "cannot smell",
    "no smell",
    "no taste",
    "cannot taste food",
    "low oxygen",
    "breathless",
    "hard to breathe",
    "gasping for air",
    "shivering",
    "chills",
    "shaking body",
    "sweating",
    "bad headache",
    "head pain",
    "pale skin",
    "yellow skin",
    "white face",
    "bloodless look",
    "bone pain",
    "skin rash",
    "red spots",
    "eye pain",
    "pain behind eyes",
    "tiny red dots",
    "low bp",
    "feeling dizzy when standing",
    "weak pulse",
    "long fever",
    "fever not going",
    "fever for days",
    "stomach pain",
    "stomach hurts",
    "belly ache",
    "white tongue",
    "dirty tongue",
    "coated tongue",
    "severe cough",
    "bad cough",
    "short of breath",
    "rattling chest",
    "chest noise",
    "fast breathing",
    "breathing very fast",
    "cough for weeks",
    "old cough",
    "coughing blood",
    "losing weight",
    "getting thin",
    "sweating at night",
    "heavy weakness",
    "wheezing",
    "whistling chest",
    "gasping",
    "tight chest",
    "whistling sound",
    "very thirsty",
    "always thirsty",
    "peeing a lot",
    "going to pee all night",
    "cuts wont heal",
    "slow healing wounds",
    "high blood sugar",
    "high bp",
    "high blood pressure",
    "severe headache",
    "bad head pain",
    "head bursting",
    "no symptoms",
    "feels normal",
    "blurry eyes",
    "dizzy",
    "feeling spinny",
    "head spinning",
    "giddy",
    "fainting",
    "passed out",
    "everything blacked out",
    "cold hands",
    "cold feet",
    "always tired",
    "no energy",
    "body feels heavy",
    "cannot work",
    "white inner eyelids",
    "pale eyes",
    "white nails",
    "extreme thirst",
    "very dry mouth",
    "no spit",
    "dark yellow urine",
    "loose potty",
    "watery potty",
    "loose motion",
    "frequent bathroom trips",
    "vomiting",
    "throwing up",
    "dry mouth",
    "fast pulse",
    "fast heartbeat",
    "watery motion",
    "nonstop potty",
    "no energy at all",
    "sunken eyes",
    "no urine",
    "not peeing",
    "passing out",
    "stomach cramps",
    "stomach twisting",
    "stomach painful to touch",
    "belly hurts when pressed",
    "sweating a lot",
    "tired in sun",
    "faint from heat",
    "cool wet skin",
    "clammy skin",
    "headache",
    "uncontrollable shivering",
    "slurred speech",
    "stuttering",
    "confused",
    "acting strange",
    "freezing cold",
    "cold skin",
    "very low body temperature",
    "slow heart",
    "intense pain",
    "skin redness",
    "blister",
    "water blisters",
    "burn",
    "fire burn",
    "hot water burn",
    "burnt area",
    "charred skin",
    "black skin",
    "peeling skin",
    "severe bone pain",
    "broken bone",
    "broken arm",
    "broken leg",
    "swelling",
    "crooked arm",
    "crooked leg",
    "bone popping out",
    "cannot move limb",
    "joint pain",
    "ankle pain",
    "wrist pain",
    "rapid swelling",
    "catch",
    "sprain",
    "twisted foot",
    "painful to touch",
    "black and blue skin",
    "bruised joint",
    "snake bite",
    "snake bit",
    "snake puncture",
    "snake teeth marks",
    "spreading swelling",
    "swelling going up",
    "cold sweat",
    "dog bite",
    "dog attacked",
    "animal teeth mark",
    "deep cut",
    "flesh torn",
    "flesh showing",
    "bone showing",
    "heavy bleeding",
    "bee sting",
    "wasp sting",
    "honeybee",
    "swelling at sting spot",
    "red lump",
    "choking",
    "scorpion",
    "scorpion sting",
    "scorpion bite",
    "extreme burning pain",
    "pain in one spot",
    "burning pain",
    "centipede bite",
    "two small dot marks",
    "local swelling",
    "severe muscle pain",
    "numbness",
    "unconscious",
    "current shock",
    "electric shock",
    "burn marks from wire",
    "stiff muscles",
    "tight body",
    "irregular heart",
    "heart jumping",
    "severe pain",
    "body part crushed",
    "body part trapped",
    "heavy weight fell on limb",
    "dark urine",
    "black urine",
    "numb limb",
    "blood spurting",
    "blood flowing fast",
    "cut finger",
    "ear pain",
    "earache",
    "red inside ear",
    "pus from ear",
    "fluid leaking from ear",
    "ear draining",
    "red eye",
    "pink eye",
    "sticky eye",
    "eye discharge",
    "infected eye",
    "red eyeballs",
    "itchy eye",
    "watery eyes",
    "sharp eye pain",
    "something in eye",
    "dirt in eye",
    "dust in eye",
    "visible speck in eye",
    "scratchy feeling",
    "red skin",
    "swollen skin",
    "boil",
    "pus",
    "skin infection",
    "warm skin",
    "hot to touch",
    "itchy circular rash",
    "round rash",
    "itchy skin",
    "ring rash",
    "ringworm",
    "circle mark on skin",
    "red border rash",
    "itching",
    "scratching",
    "scratching all night",
    "small pimples",
    "lines on skin",
    "rash between fingers",
    "burrows",
    "intense itching",
    "itching in bottom",
    "worms in potty",
    "grinding teeth at night",
    "bloated stomach",
    "swollen belly",
    "blurry vision",
    "cannot see clearly",
    "blindness",
    "fake alcohol",
    "bad liquor",
    "big wide eyes",
    "pupils not moving"
]
    user = text.lower()
    user_symp=[]
    for i in symptoms:
        if i in user:
            user_symp.append(i)
    disease = {
    "Common Cold": ["$running nose", "$watery nose", "$sneezing", "$sneeze", "$nose dripping",
                    "throat pain", "pain when swallowing", "cough", "coughing", "red throat", "fever", "warm body", "mild fever"],

    "Influenza (Flu)": ["$fever", "$hot body", "$body pain", "$body ache", "$body breaking", "$tired", "$no strength", "$weakness",
                         "cough", "sore throat", "throat pain", "fast heart", "heart beating fast", "heart racing"],

    "COVID-19": ["$fever", "$cough", "$dry cough", "$cannot smell", "$no smell", "$no taste", "$cannot taste food",
                 "low oxygen", "breathless", "hard to breathe", "gasping for air"],

    "Malaria": ["$fever", "$shivering", "$chills", "$shaking body", "$sweating", "$bad headache", "$head pain",
                "pale skin", "yellow skin", "white face", "bloodless look"],

    "Dengue Fever": ["$fever", "$bad headache", "$body pain", "$bone pain", "$skin rash", "$red spots", "$eye pain", "$pain behind eyes",
                      "tiny red dots", "low bp", "feeling dizzy when standing", "weak pulse"],

    "Typhoid Fever": ["$long fever", "$fever not going", "$fever for days", "$stomach pain", "$stomach hurts", "$belly ache",
                      "white tongue", "dirty tongue", "coated tongue"],

    "Pneumonia": ["$severe cough", "$bad cough", "$fever", "$breathlessness", "$hard to breathe", "$short of breath",
                  "rattling chest", "chest noise", "fast breathing", "breathing very fast"],

    "Tuberculosis": ["$cough for weeks", "$old cough", "$coughing blood", "$losing weight", "$getting thin", "$sweating at night",
                     "chest noise", "rattling lung", "heavy weakness"],

    "Asthma": ["$wheezing", "$whistling chest", "$cough", "$breathlessness", "$gasping", "$tight chest",
               "whistling sound", "breathing very fast", "rapid breathing"],

    "Diabetes": ["$very thirsty", "$always thirsty", "$peeing a lot", "$going to pee all night", "$losing weight",
                 "cuts wont heal", "slow healing wounds", "high blood sugar"],

    "Hypertension": ["$high bp", "$high blood pressure", "$severe headache", "$bad head pain", "$head bursting",
                     "no symptoms", "feels normal", "blurry eyes"],

    "Hypotension": ["$dizzy", "$feeling spinny", "$head spinning", "$giddy", "$fainting", "$passed out", "$everything blacked out",
                    "pale skin", "low bp", "cold hands", "cold feet"],

    "Anemia": ["$always tired", "$no energy", "$heavy weakness", "$body feels heavy", "$cannot work",
               "white inner eyelids", "pale eyes", "white nails", "fast heart"],

    "Dehydration": ["$very thirsty", "$extreme thirst", "$dizzy", "$feeling spinny",
                    "very dry mouth", "no spit", "fast heart", "low bp", "dark yellow urine"],

    "Acute Diarrhea": ["$loose potty", "$watery potty", "$loose motion", "$frequent bathroom trips", "$vomiting", "$throwing up",
                       "dry mouth", "very thirsty", "fast pulse", "fast heartbeat"],

    "Cholera": ["$loose potty", "$watery motion", "$nonstop potty", "$extreme thirst", "$no energy at all",
                "low bp", "sunken eyes", "no urine", "not peeing", "fainting", "passing out"],

    "Food Poisoning": ["$vomiting", "$throwing up", "$loose potty", "$stomach cramps", "$stomach twisting",
                       "fever", "stomach painful to touch", "belly hurts when pressed"],

    "Heat Exhaustion": ["$sweating a lot", "$dizzy", "$giddy", "$feeling spinny", "$tired in sun", "$faint from heat",
                        "cool wet skin", "clammy skin", "fast pulse", "headache"],

    "Hypothermia": ["$uncontrollable shivering", "$slurred speech", "$stuttering", "$confused", "$acting strange", "$freezing cold",
                    "cold skin", "pale skin", "very low body temperature", "slow heart"],

    "Burns": ["$intense pain", "$skin redness", "$blister", "$water blisters", "$burn", "$fire burn", "$hot water burn",
              "burnt area", "charred skin", "black skin", "peeling skin"],

    "Fracture": ["$severe bone pain", "$broken bone", "$broken arm", "$broken leg", "$swelling",
                 "crooked arm", "crooked leg", "bone popping out", "cannot move limb"],

    "Sprain": ["$joint pain", "$ankle pain", "$wrist pain", "$rapid swelling", "$catch", "$sprain", "$twisted foot",
               "painful to touch", "black and blue skin", "bruised joint"],

    "Snake Bite": ["$snake bite", "$snake bit", "$snake puncture", "$snake teeth marks",
                   "spreading swelling", "swelling going up", "fainting", "cold sweat", "hard to breathe"],

    "Dog Bite": ["$dog bite", "$dog attacked", "$animal teeth mark", "$deep cut",
                 "flesh torn", "flesh showing", "bone showing", "heavy bleeding"],

    "Bee/Wasp Sting": ["$bee sting", "$wasp sting", "$honeybee",
                       "swelling at sting spot", "red lump", "low bp", "choking", "hard to breathe"],

    "Scorpion Sting": ["$scorpion", "$scorpion sting", "$scorpion bite",
                       "fast heart", "extreme burning pain", "sweating a lot"],

    "Centipede Bite": ["$pain in one spot", "$burning pain", "$centipede bite",
                       "two small dot marks", "local swelling", "fast heart"],

    "Electric Shock": ["$severe muscle pain", "$numbness", "$passed out", "$unconscious", "$current shock", "$electric shock",
                       "burn marks from wire", "stiff muscles", "tight body", "irregular heart", "heart jumping"],

    "Crush Injury": ["$severe pain", "$body part crushed", "$body part trapped", "$heavy weight fell on limb",
                     "dark urine", "black urine", "fast heart", "low bp", "numb limb"],

    "Severe Bleeding / Amputation": ["$heavy bleeding", "$blood spurting", "$blood flowing fast", "$dizzy", "$cold sweat", "$deep cut", "$cut finger",
                                     "flesh torn", "fast heart", "weak pulse", "low bp", "passing out"],

    "Ear Infection": ["$ear pain", "$earache", "$fever",
                      "red inside ear", "pus from ear", "fluid leaking from ear", "ear draining"],

    "Conjunctivitis": ["$red eye", "$pink eye", "$sticky eye", "$eye discharge", "$infected eye",
                       "red eyeballs", "itchy eye", "watery eyes"],

    "Foreign Body in Eye": ["$sharp eye pain", "$something in eye", "$dirt in eye", "$dust in eye",
                            "visible speck in eye", "scratchy feeling", "red eye"],

    "Skin Infection": ["$red skin", "$swelling", "$swollen skin", "$pain in one spot", "$boil", "$pus", "$skin infection",
                       "warm skin", "hot to touch", "mild fever"],

    "Fungal Infection": ["$itchy circular rash", "$round rash", "$itchy skin", "$ring rash",
                         "ringworm", "circle mark on skin", "red border rash"],

    "Scabies": ["$itching", "$scratching", "$scratching all night", "$skin rash", "$small pimples",
                "lines on skin", "rash between fingers", "burrows"],

    "Worm Infestation": ["$stomach pain", "$belly ache", "$intense itching", "$itching in bottom", "$losing weight", "$getting thin",
                         "worms in potty", "grinding teeth at night", "bloated stomach", "swollen belly"],

    "Methanol Poisoning": ["$blurry vision", "$cannot see clearly", "$blindness", "$stomach pain", "$vomiting", "$fake alcohol", "$bad liquor",
                           "big wide eyes", "pupils not moving", "gasping for air", "low bp"]
    }
    score = {
    "Common Cold": 0,
    "Influenza (Flu)": 0,
    "COVID-19": 0,
    "Malaria": 0,
    "Dengue Fever": 0,
    "Typhoid Fever": 0,
    "Pneumonia": 0,
    "Tuberculosis": 0,
    "Asthma": 0,
    "Diabetes": 0,
    "Hypertension": 0,
    "Hypotension": 0,
    "Anemia": 0,
    "Dehydration": 0,
    "Acute Diarrhea": 0,
    "Cholera": 0,
    "Food Poisoning": 0,
    "Heat Exhaustion": 0,
    "Hypothermia": 0,
    "Burns": 0,
    "Fracture": 0,
    "Sprain": 0,
    "Snake Bite": 0,
    "Dog Bite": 0,
    "Bee/Wasp Sting": 0,
    "Scorpion Sting": 0,
    "Centipede Bite": 0,
    "Electric Shock": 0,
    "Crush Injury": 0,
    "Severe Bleeding / Amputation": 0,
    "Ear Infection": 0,
    "Conjunctivitis": 0,
    "Foreign Body in Eye": 0,
    "Skin Infection": 0,
    "Fungal Infection": 0,
    "Scabies": 0,
    "Worm Infestation": 0,
    "Methanol Poisoning": 0
}
    keys=list(disease)
    for i in keys:
        count=0
        samp_disease= disease[i]
        for j in user_symp:
            for k in samp_disease:
                if j in k and '$'in k:
                    count+=5
                elif j in k:
                    count+=1
        score[i]=count
    max_score=0  
    index = []
    for i in keys:
        if score[i]>max_score:
            max_score = score[i]
    for i in keys:
        if score[i]==max_score:
            index.append(i)
    cure = {
    "Common Cold": "Rest, stay hydrated, and consider over-the-counter cold remedies. If symptoms persist or worsen, consult a healthcare professional.",
    "Influenza (Flu)": "Rest, stay hydrated, and consider over-the-counter flu remedies. If symptoms persist or worsen, consult a healthcare professional.",
    "COVID-19": "Rest, stay hydrated, and consider over-the-counter COVID-19 remedies. If symptoms persist or worsen, consult a healthcare professional.",
    "Malaria": "Cured with antimalarial drugs (Artemisinin-based).",
    "Dengue Fever": "Managed with supportive care (rest, fluids, pain relief).",
    "Typhoid Fever": "Cured with antibiotics (Ciprofloxacin, Azithromycin).",
    "Pneumonia": "Managed with antibiotics (Amoxicillin, Azithromycin).",
    "Tuberculosis": "Cured with a combination of antibiotics (Isoniazid, Rifampin, Ethambutol, Pyrazinamide).",
    "Asthma": "Managed with rescue inhalers (albuterol) and steroids.",
    "Diabetes": "Managed with insulin therapy and lifestyle modifications.",
    "Hypertension": "Managed with antihypertensive medications and lifestyle modifications.",
    "Hypotension": "Managed with fluid replacement and compression stockings.",
    "Anemia": "Managed with iron supplements and dietary modifications.",
    "Dehydration": "Managed with fluid replacement and electrolyte balance.",
    "Acute Diarrhea": "Managed with fluid replacement and dietary modifications.",
    "Cholera": "Cured with antibiotics (Doxycycline, Zithromycin) and fluid replacement.",
    "Food Poisoning": "Managed with supportive care (rest, fluids, pain relief).",
    "Heat Exhaustion": "Managed with rest, fluids, and cooling measures.",
    "Hypothermia": "Managed with warming measures and fluid replacement.",
    "Burns": "Managed with wound care and pain relief.",
    "Fracture": "Managed with immobilization and pain relief.",
    "Sprain": "Managed with rest, ice, compression, and elevation.",
    "Snake Bite": "Managed with antivenom and supportive care.",
    "Dog Bite": "Managed with wound cleaning and rabies vaccination.",
    "Bee/Wasp Sting": "Managed with antihistamines and pain relief.",
    "Scorpion Sting": "Managed with antivenom and supportive care.",
    "Centipede Bite": "Managed with pain relief and monitoring for allergic reactions.",
    "Electric Shock": "Managed with cardiac monitoring and supportive care.",
    "Severe Bleeding / Amputation": "Managed with emergency care and surgical intervention.",
    "Ear Infection": "Managed with antibiotics and pain relief.",
    "Conjunctivitis": "Managed with antibiotic eye drops and supportive care.",
    "Foreign Body in Eye": "Managed with removal of the object and antibiotic treatment.",
    "Skin Infection": "Managed with topical or systemic antibiotics.",
    "Fungal Infection": "Managed with antifungal medications.",
    "Scabies": "Managed with topical scabicides and hygiene measures.",
    "Worm Infestation": "Managed with anthelmintic drugs.",
    "Methanol Poisoning": "Managed with ethanol administration and supportive care."
}
    disease_detected = index[0]
    if max_score == 0:
        return 'You said: '+text+' Disease detected: None cure: None'
    else:
        return 'You said: '+text+' symptoms detected: '+', '.join(user_symp)+' Disease detected: '+disease_detected+' cure: '+cure[disease_detected] 
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