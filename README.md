# Chatbot-v0.1
MediBot is a friendly, Flask-powered assistant designed to provide quick first aid tips. It offers clear guidance on everything from snake bites and choking to recognizing heart attack symptoms and managing daily stress. With a clean Python backend and a simple web interface, it’s a helpful, accessible tool for anyone exploring health-tech.

Features :-
Instant First Aid Guidance: Provides step-by-step instructions for wounds, burns, choking (Heimlich maneuver), and animal bites.
Emergency Recognition: Identifies symptoms for critical conditions like heart attacks, strokes, and rabies.
Health & Wellness Tips: Offers advice on managing stress, anxiety, headaches, and the common cold.
Vital Stats Reference: Lists ideal blood pressure ranges for children, adults, and the elderly.
Responsive UI: A clean, modern chat interface built with HTML5, CSS3, and Bootstrap.

Tech Stack:-

Backend: Python, Flask
Frontend: HTML5, CSS3, JavaScript (Vanilla)
API: RESTful API with Flask-CORS for cross-origin communication.
Styling: Bootstrap 5 & FontAwesome.

Installation & Setup:-

Follow these steps to get the project running locally:
1. Clone the repository
Bash
git clone https://github.com/your-username/medibot.git
cd medibot
2. Set up the Backend
Ensure you have Python installed. It is recommended to use a virtual environment.

Bash
# Install dependencies
pip install flask flask-cors

# Run the server
python chatbot.py
The Flask server will start on http://127.0.0.1:5000.

3. Run the Frontend
Simply open Workshop.html in your preferred web browser. Make sure the Flask server is running in the background so the chatbot can respond.

How it Works:-

The Frontend (Workshop.html) captures user input and sends a POST request to the /chat endpoint.
The Backend (chatbot.py) processes the string using keyword matching to find the most relevant medical advice.
The UI dynamically updates the chat window with the response, automatically scrolling to the latest message.

⚠️ Disclaimer
This chatbot is for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
