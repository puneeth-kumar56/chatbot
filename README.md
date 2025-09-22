# chatbot

Rule-Based Chatbot 🤖

A simple rule-based chatbot built with Python.
This chatbot uses if-else logic and predefined keyword-matching rules to simulate conversations with a user.

✨ Features

Responds to greetings (e.g., "hello", "hi").

Handles farewells (e.g., "bye", "exit").

Answers questions like:

"How are you?"

"What is your name?"

"What can you do?"

"How old are you?"

Recognizes keywords like weather, time, age, hobby, AI, robot, good, bad, thank you.

Provides default fallback responses for unknown inputs.

🛠️ Requirements

Python 3.x (tested on 3.8+).

No external dependencies (uses only built-in libraries: random and re).

🚀 How to Run

Run the chatbot:

python chatbot.py


Start chatting! Example:

==================================================
Welcome to ChatBot!
Type 'quit', 'exit', or 'bye' to end the conversation.
==================================================

You: hello
ChatBot: Hi there! Nice to meet you!

You: what is your name?
ChatBot: My name is ChatBot! I'm a simple rule-based chatbot.

You: bye
ChatBot: See you later! Have a great day!

📂 File Structure
rule-based-chatbot/
│
├── chatbot.py    # Main chatbot implementation
└── README.md     # Project documentation

🧠 How It Works

Preprocessing: User input is converted to lowercase and stripped of extra spaces.

Rule Matching: The chatbot checks input against predefined lists of keywords.

Responses: If a match is found, it returns a random response from a response set. Otherwise, a fallback reply is given.

📌 Example Interactions

Greeting

You: hi
ChatBot: Greetings! What would you like to talk about?


Farewell

You: exit
ChatBot: Goodbye! It was nice chatting with you!


Unknown Input

You: tell me about space
ChatBot: That's interesting! Can you tell me more?
