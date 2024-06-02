import random
import webbrowser

responses = {
    'hi': ['Hello!', 'Hi there!', 'Hey!', 'Greetings!', 'Salutations!', 'Howdy!', 'Hiya!', 'Hola!', 'Good to see you!', 'Hey, what\'s up?'],
    'how are you': ['I am doing well, thank you!', 'I am fine, thank you for asking!', 'I am good, how about you?', 'I am great!', 'Feeling awesome!', 'I am just a computer program, but thanks for asking!', 'All systems operational!', 'I am here to help!', 'Ready and willing!', 'I\'m fantastic!'],
    'what is your name': ['My name is Chatbot.', 'I am Chatbot.', 'You can call me Chatbot.', 'I am your friendly Chatbot.', 'Chatbot at your service.', 'I go by Chatbot.', 'Chatbot is my name.', 'I am called Chatbot.', 'I am known as Chatbot.', 'Chatbot here!'],
    # Add more responses...
}

website_commands = {
    'youtube': 'https://www.youtube.com/',
    'open python website': 'https://www.python.org/',
    # Add more website commands...
}

def handle_input(user_input):
    user_input = user_input.lower().strip('/')

    if user_input in responses:
        return random.choice(responses[user_input])
    elif user_input in website_commands:
        webbrowser.open(website_commands[user_input])
        return f"Opening {user_input}..."
    else:
        return "I'm sorry, I didn't understand that."

# Example usage
while True:
    user_input = input('Enter a command: ')
    chatbot_response = handle_input(user_input)
    print('DFS Chat:', chatbot_response)
