from flask_cors import CORS
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)

def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in ['exit', 'quit', 'bye']:
        return "Goodbye! Have a great day!"
    elif "hello" in user_input or "hi" in user_input:
        return "Hello there! How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm doing great! Thanks for asking."
    elif "what's your name" in user_input or "who are you" in user_input:
        return "I'm your friendly chatbot, here to assist you with anything you need!"
    elif "help" in user_input:
        return "Sure! I can help you with a variety of tasks. Just ask me anything!"
    elif "what can you do" in user_input:
        return "I can answer your questions, provide information, and assist you with various tasks. Just let me know what you need!"
    elif "emergency number" in user_input:
        return "The emergency number is 108. Please call it if you are in a medical emergency situation."
    elif "wound care" in user_input:
        return "For wound care, it's important to clean the wound with mild soap and water, apply an antibiotic ointment, and cover it with a sterile bandage. If the wound is deep or shows signs of infection, please seek medical attention."
    elif"symptoms of infection" in user_input:
        return "Chatbot: Symptoms of infection can include redness, swelling, warmth around the wound, pus or discharge, and fever. If you notice any of these symptoms, it's important to seek medical attention."
    elif "when to seek medical attention" in user_input:
        return "Chatbot: You should seek medical attention if the wound is deep, won't stop bleeding, shows signs of infection, or if you have any concerns about your health. It's always better to be safe and get professional advice."
    elif "suicide helpline" in user_input:
        return "Chatbot: If you are in crisis, please call the suicide helpline at 1-800-273-8255."
    elif "feeling cold" in user_input:
        return "Chatbot: If you're feeling cold, try to warm up by putting on more clothes or finding a warmer place. "
    elif "treatment for common cold" in user_input or "common cold treatment" in user_input:
        return "Chatbot: The treatment for a common cold typically includes rest, staying hydrated, and using over-the-counter medications to relieve symptoms. If symptoms persist or worsen, please consult a healthcare professional."
    elif "temperature rising" in user_input or "feeling hot" in user_input:
        return "Chatbot: If you're feeling hot, try to cool down by removing excess clothing, staying in a cool environment, or using a fan."
    elif "headache" in user_input:
        return "Chatbot: For a headache, you can try resting in a quiet, dark room, applying a cold compress to your forehead, and taking over-the-counter pain relievers. If the headache is severe or persistent, please consult a healthcare professional."
    elif "stomach ache" in user_input:
        return "Chatbot: For a stomach ache, you can try resting, drinking clear fluids, and avoiding solid foods until you feel better. If the stomach ache is severe or persistent, please consult a healthcare professional."
    elif "feeling anxious" in user_input:
        return "Chatbot: If you're feeling anxious, try taking deep breaths, practicing mindfulness, or engaging in activities that you enjoy. If your anxiety is severe or persistent, please consider seeking support from a mental health professional."
    elif "feeling depressed" in user_input:
        return "Chatbot: If you're feeling depressed, it's important to reach out for support. Consider talking to a trusted friend, family member, or mental health professional. Remember, you're not alone and there are people who care about you."
    elif "feeling stressed" in user_input:
        return "Chatbot: If you're feeling stressed, try taking breaks, practicing relaxation techniques, or engaging in activities that you enjoy. If your stress is severe or persistent, please consider seeking support from a mental health professional."
    elif "snake bite" in user_input:
       return "Chatbot: If you or someone else has been bitten by a snake, identify the snake if possible or note its characteristics. Try to keep the affected limb immobilized and at or below heart level, and avoid applying ice or a tourniquet."
    elif "antivenom" in user_input:
       return "Chatbot: Antivenom is a treatment used to counteract the effects of venom from snake bites. To find the correct antivenom, identify the reptile that caused the bite, better if you know its breed. It is typically administered in a hospital setting and should be given as soon as possible after a snake bite to be most effective."
    elif "first aid for snake bite" in user_input:
       return "Chatbot: First aid for a snake bite includes keeping the victim calm and still, immobilizing the affected limb, and seeking immediate medical attention. Do not attempt to suck out the venom or apply a tourniquet."
    elif "symptoms of snake bite" in user_input:
        return "Chatbot: Symptoms of a snake bite can include pain and swelling at the bite site, redness, bruising, nausea, vomiting, difficulty breathing, and in severe cases, paralysis. If you experience any of these symptoms after a snake bite, seek medical attention immediately."
    elif "prevention of snake bites" in user_input:
        return "Chatbot: To prevent snake bites, avoid walking in tall grass or areas where snakes may be hiding, wear protective footwear and clothing when hiking, and be cautious when handling firewood or debris. If you encounter a snake, give it plenty of space and do not attempt to handle it."
    elif "dog bite" in user_input or "bit by a dog" in user_input:
       return "Chatbot: If you or someone else has been bitten by a dog, clean the wound thoroughly with soap and water, apply an antiseptic, and seek medical attention if the bite is deep or if the dog's vaccination status is unknown."
    elif "cat bite" in user_input or "bit by a cat" in user_input:
        return "Chatbot: If you or someone else has been bitten by a cat, clean the wound thoroughly with soap and water, apply an antiseptic, and seek medical attention if the bite is deep or if you notice signs of infection."
    elif "cat scratched" in user_input or "scratched by a cat" in user_input:
        return "Chatbot: If you or someone else has been scratched by a cat, clean the wound thoroughly with soap and water, apply an antiseptic, and monitor for signs of infection. If you notice redness, swelling, or pus, seek medical attention."
    elif "wild animal bit" in user_input or "bit by a wild animal" in user_input:
        return "Chatbot: If you or someone else has been bitten by a wild animal, clean the wound thoroughly with soap and water, apply an antiseptic, and seek medical attention immediately. It's important to identify the animal if possible, as it may require specific treatment."
    elif "rabies" in user_input:
        return "Chatbot: Rabies is a viral disease that can be transmitted through the bite of an infected animal. If you have been bitten by an animal that may have rabies, seek medical attention immediately. Rabies can be prevented with prompt treatment, including a series of vaccinations."
    elif "rabies vaccination" in user_input:
        return "Chatbot: If you have been exposed to an animal that may have rabies, it's important to seek medical attention immediately. A healthcare professional will assess your risk and may recommend a series of rabies vaccinations to prevent the disease."
    elif "rabies symptoms" in user_input:
        return "Chatbot: Symptoms of rabies can include fever, headache, muscle weakness, and in later stages, confusion, agitation, and difficulty swallowing. If you experience any of these symptoms after being bitten by an animal, seek medical attention immediately."
    elif "rabies prevention" in user_input:
        return "Chatbot: To prevent rabies, avoid contact with wild animals, ensure your pets are vaccinated against rabies, and seek medical attention immediately if you are bitten by an animal that may have rabies."
    elif "rabies vaccination schedule" in user_input:
        return "Chatbot: The rabies vaccination schedule typically includes a series of three doses given on days 0, 3, and 7 after exposure. In some cases, additional doses may be recommended based on the individual's risk and response to the vaccine."
    elif "rabies vaccination window" in user_input:
        return "Chatbot: The rabies vaccination window is ideally within 24 hours of exposure to the virus. However, it can still be effective if administered within a few days after exposure. It's important to seek medical attention as soon as possible after a potential rabies exposure to ensure timely treatment."
    elif "poisoning" in user_input:
        return "Chatbot: If you suspect poisoning, call your local poison control center immediately for guidance. Do not induce vomiting unless instructed to do so by a medical professional."
    elif "overdose" in user_input:
        return "Chatbot: If you suspect an overdose, call emergency services immediately. Provide as much information as possible about the substance involved and the person's condition."
    elif "burns" in user_input:
        return "Chatbot: For burns, cool the burn with running water for at least 10 minutes, cover it with a sterile bandage, and seek medical attention if the burn is severe or if you notice signs of infection."
    elif "types of burns" in user_input:
        return "Chatbot: There are three main types of burns: first-degree burns, which affect only the outer layer of skin; second-degree burns, which affect both the outer and underlying layers of skin; and third-degree burns, which affect all layers of skin and may require skin grafts for healing."
    elif "burn treatment" in user_input:
        return "Chatbot: Treatment for burns depends on the severity. For minor burns, cool the burn with running water, cover it with a sterile bandage, and take over-the-counter pain relievers if needed. For more severe burns, seek medical attention immediately."
    elif "blisters" in user_input:
        return "Chatbot: Blisters are small pockets of fluid that form on the skin due to friction or burns. To treat blisters, keep the area clean and dry, avoid popping the blister, and cover it with a sterile bandage if necessary. If the blister is large or painful, seek medical attention."
    elif "sunburn" in user_input:
        return "Chatbot: For sunburn, cool the skin with running water, apply aloe vera or a moisturizing lotion, and take over-the-counter pain relievers if needed. To prevent sunburn, use sunscreen with a high SPF, wear protective clothing, and avoid prolonged sun exposure."
    elif "sunburn prevention" in user_input:
        return "Chatbot: To prevent sunburn, use sunscreen with a high SPF, wear protective clothing such as hats and long sleeves, seek shade during peak sun hours, and avoid prolonged sun exposure."
    elif "sunburn treatment" in user_input:
        return "Chatbot: For sunburn treatment, cool the skin with running water, apply aloe vera or a moisturizing lotion, and take over-the-counter pain relievers if needed. If the sunburn is severe or if you notice signs of infection, seek medical attention."
    elif "first degree burn" in user_input:
        return "Chatbot: A first-degree burn affects only the outer layer of skin and typically causes redness and pain. Treatment includes cooling the burn with running water, applying aloe vera or a moisturizing lotion, and taking over-the-counter pain relievers if needed."
    elif "second degree burn" in user_input:
        return "Chatbot: A second-degree burn affects both the outer and underlying layers of skin and can cause redness, swelling, and blistering. Treatment includes cooling the burn with running water, covering it with a sterile bandage, and seeking medical attention if the burn is severe."
    elif "third degree burn" in user_input:
        return "Chatbot: A third-degree burn affects all layers of skin and can cause white or charred skin. Treatment typically requires immediate medical attention and may involve skin grafts for healing."
    elif "chemical burn" in user_input:
        return "Chatbot: For chemical burns, immediately flush the affected area with running water for at least 20 minutes. Remove any contaminated clothing and seek medical attention as soon as possible."
    elif "electrical burn" in user_input:
        return "Chatbot: For electrical burns, ensure the source of electricity is turned off before providing assistance. Call emergency services immediately and do not touch the person until the electricity is off. Electrical burns can cause internal injuries, so it's important to seek medical attention even if the burn appears minor."
    elif "first aid for burns" in user_input:
        return "Chatbot: First aid for burns includes cooling the burn with running water, covering it with a sterile bandage, and seeking medical attention if the burn is severe or if you notice signs of infection. Avoid applying ice or butter to the burn, as this can cause further damage."
    elif "choked" in user_input or "choking" in user_input:
        return "Chatbot: If someone is choking, encourage them to cough to try to dislodge the object. If they cannot breathe, speak, or cough, call emergency services immediately and perform the Heimlich maneuver if you are trained to do so."
    elif "heimlich maneuver" in user_input:
        return "Chatbot: The Heimlich maneuver is a first aid technique used to treat choking. To perform the Heimlich maneuver, stand behind the person and wrap your arms around their waist. Make a fist with one hand and place it just above the person's navel. Grasp your fist with your other hand and give quick, upward thrusts until the object is expelled or the person can breathe again."
    elif "cpr" in user_input:
        return "Chatbot: CPR, or cardiopulmonary resuscitation, is a life-saving technique used in emergencies when someone's heartbeat or breathing has stopped. To perform CPR, check for responsiveness and breathing, call emergency services, and begin chest compressions at a rate of 100-120 compressions per minute. If you are trained in CPR, you can also provide rescue breaths after every 30 compressions."
    elif "first aid for choking" in user_input:
        return "Chatbot: First aid for choking includes encouraging the person to cough, calling emergency services if they cannot breathe, speak, or cough, and performing the Heimlich maneuver if you are trained to do so."
    elif "first aid for cpr" in user_input:
        return "Chatbot: First aid for CPR includes checking for responsiveness and breathing, calling emergency services, and beginning chest compressions at a rate of 100-120 compressions per minute. If you are trained in CPR, you can also provide rescue breaths after every 30 compressions."
    elif "ideal blood pressure for adult male" in user_input:
        return "Chatbot: The ideal blood pressure for an adult male is typically around 120/80 mmHg. However, it's important to note that individual blood pressure can vary based on factors such as age, health conditions, and lifestyle."
    elif "ideal blood pressure for adult female" in user_input:
        return "Chatbot: The ideal blood pressure for an adult female is around 120/80 mmHg. However, it's important to note that individual blood pressure can vary based on factors such as age, health conditions, and lifestyle."
    elif "ideal blood pressure for children" in user_input:
        return "Chatbot: The ideal blood pressure for children varies based on age, height, and gender. Generally, for children aged 1-5 years, the average blood pressure is around 90/60 mmHg. For children aged 6-13 years, the average blood pressure is around 110/70 mmHg. It's important to consult with a healthcare professional for specific blood pressure guidelines for children."
    elif "ideal blood pressure for elderly" in user_input:
        return "Chatbot: The ideal blood pressure for elderly individuals can vary, but generally, a blood pressure of around 120/80 mmHg is considered healthy. However, it's important to consult with a healthcare professional for personalized blood pressure targets based on individual health conditions and risk factors."
    elif "high blood pressure" in user_input or "hypertension" in user_input:
        return "Chatbot: High blood pressure, or hypertension, is a condition where the force of the blood against the artery walls is too high. It can increase the risk of heart disease and stroke. Lifestyle changes such as a healthy diet, regular exercise, and stress management can help manage high blood pressure. In some cases, medication may be necessary."
    elif "low blood pressure" in user_input or "hypotension" in user_input:
        return "Chatbot: Low blood pressure, or hypotension, is a condition where the blood pressure is lower than normal. It can cause symptoms such as dizziness, fainting, and fatigue. If you experience symptoms of low blood pressure, it's important to consult with a healthcare professional for proper diagnosis and treatment."
    elif "normal blood pressure" in user_input:
        return "Chatbot: Normal blood pressure is typically around 120/80 mmHg. However, it's important to note that individual blood pressure can vary based on factors such as age, health conditions, and lifestyle."
    elif "heart attack" in user_input:
        return "Chatbot: A heart attack occurs when the blood flow to a part of the heart is blocked, usually by a blood clot. Symptoms can include chest pain, shortness of breath, nausea, and pain in the arms or jaw. If you suspect someone is having a heart attack, call emergency services immediately."
    elif "stroke" in user_input:
        return "Chatbot: A stroke occurs when the blood supply to part of the brain is interrupted or reduced, preventing brain tissue from getting oxygen and nutrients. Symptoms can include sudden numbness or weakness in the face, arm, or leg, especially on one side of the body, sudden confusion, trouble speaking or understanding speech, and sudden trouble seeing in one or both eyes. If you suspect someone is having a stroke, call emergency services immediately."
    elif "diabetes" in user_input:
        return "Chatbot: Diabetes is a chronic condition that affects how your body processes blood sugar (glucose). There are two main types of diabetes: Type 1, where the body does not produce insulin, and Type 2, where the body does not use insulin properly. Managing diabetes typically involves lifestyle changes such as a healthy diet, regular exercise, and monitoring blood sugar levels. In some cases, medication or insulin therapy may be necessary."
    elif "asthma" in user_input:
        return "Chatbot: Asthma is a chronic respiratory condition that causes inflammation and narrowing of the airways, leading to difficulty breathing. Symptoms can include wheezing, coughing, shortness of breath, and chest tightness. Asthma can be managed with medications such as inhalers and by avoiding triggers that can cause symptoms."
    elif "having a heart attack" in user_input:
        return "Chatbot: If you or someone else is having a heart attack, call emergency services immediately. Chew and swallow an aspirin if you are not allergic, and try to stay calm while waiting for help to arrive."
    elif "having a stroke" in user_input:
        return "Chatbot: If you or someone else is having a stroke, call emergency services immediately. Try to note the time when symptoms started, as this information can be important for treatment decisions."
    elif "having an asthma attack" in user_input:
        return "Chatbot: If you or someone else is having an asthma attack, use a rescue inhaler if you have one, and call emergency services if symptoms are severe or do not improve."
    elif "symptoms of heart attack" in user_input or "signs of heart attack" in user_input or "heart attack symptoms" in user_input:
        return "Chatbot: Symptoms of a heart attack can include chest pain, shortness of breath, nausea, and pain in the left arm or jaw. If you suspect someone is having a heart attack, call emergency services immediately."
    elif "symptoms of stroke" in user_input or "signs of stroke" in user_input or "stroke symptoms" in user_input:
        return "Chatbot: Symptoms of a stroke can include sudden numbness or weakness in the face, arm, or leg, especially on one side of the body, sudden confusion, trouble speaking or understanding speech, and sudden trouble seeing in one or both eyes. If you suspect someone is having a stroke, call emergency services immediately."
    elif "symptoms of diabetes" in user_input or "signs of diabetes" in user_input or "diabetes symptoms" in user_input:
        return "Chatbot: Symptoms of diabetes can include increased thirst, frequent urination, extreme hunger, unexplained weight loss, fatigue, and blurred vision. If you experience any of these symptoms, it's important to consult with a healthcare professional for proper diagnosis and treatment."
    elif "symptoms of asthma" in user_input or "signs of asthma" in user_input or "asthma symptoms" in user_input:
        return "Chatbot: Symptoms of asthma can include wheezing, coughing, shortness of breath, and chest tightness. If you experience any of these symptoms, it's important to consult with a healthcare professional for proper diagnosis and treatment."
    elif "fractured bone" in user_input or "broken bone" in user_input:
        return "Chatbot: If you suspect a fractured or broken bone, it's important to immobilize the affected area and seek medical attention immediately. Avoid trying to realign the bone yourself, and if possible, apply ice to reduce swelling."
    elif "sprained ankle" in user_input:
        return "Chatbot: For a sprained ankle, it's important to rest the ankle, apply ice to reduce swelling, compress it with an elastic bandage, and elevate it above heart level. If the pain is severe or if you have difficulty walking, seek medical attention."
    elif "burning sensation" in user_input:
        return "Chatbot: A burning sensation can be caused by various factors such as nerve damage, infections, or skin conditions. If you are experiencing a burning sensation, it's important to consult with a healthcare professional for proper diagnosis and treatment."
    elif "numbness" in user_input:
        return "Chatbot: Numbness can be caused by various factors such as nerve compression, poor circulation, or certain medical conditions. If you are experiencing numbness, it's important to consult with a healthcare professional for proper diagnosis and treatment."
    elif "dizziness" in user_input:
        return "Chatbot: Dizziness can be caused by various factors such as dehydration, low blood pressure, or inner ear problems. If you are experiencing dizziness, it's important to sit or lie down until it passes, and consult with a healthcare professional if it persists or is accompanied by other symptoms."
    elif "fainting" in user_input or "syncope" in user_input:
        return "Chatbot: Fainting, or syncope, is a temporary loss of consciousness usually caused by a drop in blood flow to the brain. If you or someone else faints, it's important to lie down and elevate the legs to improve blood flow. If the person does not regain consciousness within a minute or if they have other symptoms such as chest pain or difficulty breathing, seek medical attention immediately."
    elif "adhd" in user_input:
        return "Chatbot: ADHD, or Attention Deficit Hyperactivity Disorder, is a neurodevelopmental disorder characterized by symptoms of inattention, hyperactivity, and impulsivity. It can affect both children and adults. Treatment typically includes a combination of behavioral therapy, lifestyle changes, and medication."
    elif "autism" in user_input:
        return "Chatbot: Autism, or Autism Spectrum Disorder (ASD), is a developmental disorder that affects communication and behavior. It is characterized by difficulties with social interaction, repetitive behaviors, and limited interests. Early diagnosis and intervention can help improve outcomes for individuals with autism."
    elif "cartilage injury" in user_input:
        return "Chatbot: A cartilage injury can occur in joints such as the knee or shoulder. Treatment may include rest, physical therapy, and in some cases, surgery. If you suspect a cartilage injury, it's important to consult with a healthcare professional for proper diagnosis and treatment."
    elif "meniscus tear" in user_input:
        return "Chatbot: A meniscus tear is a common knee injury that can cause pain, swelling, and difficulty moving the knee. Treatment may include rest, physical therapy, and in some cases, surgery. If you suspect a meniscus tear, it's important to consult with a healthcare professional for proper diagnosis and treatment."
    elif "ligament injury" in user_input:
        return "Chatbot: A ligament injury can occur in joints such as the knee or ankle. Treatment may include rest, physical therapy, and in some cases, surgery. If you suspect a ligament injury, it's important to consult with a healthcare professional for proper diagnosis and treatment."
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you have any more questions, feel free to ask."       
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"
        
def chatbot_click():
            print("Hello! I'm your friendly chatbot. How can I assist you today?")
            while True:
                user_input = input("You: ")
                response = chatbot_response(user_input)
                print(f"Chatbot: {response}")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("msg", "")
    response = chatbot_response(user_input)
    return jsonify({"reply": response})


if __name__ == "__main__":
    app.run(debug=True)
