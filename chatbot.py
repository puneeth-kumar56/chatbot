import random
import re

class RuleBasedChatbot:
    def __init__(self):
        self.name = "ChatBot"
        self.greetings = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
        self.farewells = ["bye", "goodbye", "see you", "farewell", "quit", "exit"]
        self.how_are_you = ["how are you", "how do you do", "how's it going", "what's up"]
        self.name_questions = ["what is your name", "what's your name", "who are you", "your name"]
        
    def preprocess_input(self, user_input):
        """Clean and normalize user input"""
        return user_input.lower().strip()
    
    def get_response(self, user_input):
        """Generate response based on user input using if-else logic"""
        processed_input = self.preprocess_input(user_input)
        
        
        if any(greeting in processed_input for greeting in self.greetings):
            responses = [
                f"Hello! I'm {self.name}. How can I help you today?",
                "Hi there! Nice to meet you!",
                "Greetings! What would you like to talk about?",
                "Hello! I'm here to chat with you."
            ]
            return random.choice(responses)
        
        
        elif any(farewell in processed_input for farewell in self.farewells):
            responses = [
                "Goodbye! It was nice chatting with you!",
                "See you later! Have a great day!",
                "Farewell! Come back anytime!",
                "Bye! Take care!"
            ]
            return random.choice(responses)
        
        
        elif any(question in processed_input for question in self.how_are_you):
            responses = [
                "I'm doing great, thank you for asking! How about you?",
                "I'm fine! Ready to help you with anything you need.",
                "I'm doing well! What's on your mind today?",
                "Great! Thanks for asking. How are you doing?"
            ]
            return random.choice(responses)
        
        
        elif any(name_q in processed_input for name_q in self.name_questions):
            return f"My name is {self.name}! I'm a simple rule-based chatbot."
        
        
        elif "weather" in processed_input:
            return "I don't have access to real weather data, but I hope it's nice where you are!"
        
    
        elif "time" in processed_input or "what time" in processed_input:
            return "I don't have access to real-time data, but you can check your device's clock!"
        
    
        elif "help" in processed_input or "what can you do" in processed_input:
            return ("I can chat with you about various topics! I can respond to greetings, "
                   "tell you my name, and have simple conversations. Try asking me about myself!")
        
        
        elif "age" in processed_input or "old" in processed_input:
            return "I'm a computer program, so I don't have an age in the traditional sense!"
        
    
        elif "hobby" in processed_input or "like" in processed_input:
            return "I enjoy chatting with people and learning about different topics!"
        
        
        elif "thank" in processed_input:
            responses = [
                "You're welcome!",
                "Happy to help!",
                "No problem at all!",
                "Glad I could assist!"
            ]
            return random.choice(responses)
        
        elif any(word in processed_input for word in ["good", "great", "awesome", "fantastic", "wonderful"]):
            return "That's wonderful to hear! I'm glad things are going well for you."
        
        elif any(word in processed_input for word in ["bad", "terrible", "awful", "sad", "upset"]):
            return "I'm sorry to hear that. I hope things get better for you soon!"
        
        elif "robot" in processed_input or "ai" in processed_input or "artificial" in processed_input:
            return "Yes, I'm a simple AI chatbot! I use rules and if-else statements to respond to you."
        
        else:
            default_responses = [
                "That's interesting! Can you tell me more?",
                "I'm not sure I understand completely. Could you rephrase that?",
                "Hmm, that's a good point. What do you think about it?",
                "I'd love to learn more about that topic!",
                "That sounds intriguing! Can you elaborate?",
                "I'm still learning. Could you ask me something else?",
                "Interesting perspective! What made you think of that?"
            ]
            return random.choice(default_responses)

def main():
    """Main function to run the chatbot"""
    chatbot = RuleBasedChatbot()
    
    print("="*50)
    print(f"Welcome to {chatbot.name}!")
    print("Type 'quit', 'exit', or 'bye' to end the conversation.")
    print("="*50)
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower().strip() in ['quit', 'exit', 'bye', 'goodbye']:
            print(f"{chatbot.name}: {chatbot.get_response(user_input)}")
            break
        
        response = chatbot.get_response(user_input)
        print(f"{chatbot.name}: {response}")

if __name__ == "__main__":
    main()
