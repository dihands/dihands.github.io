ID = input('Enter ID : ')
passwd = input('Enter passwd : ')

import random

# Define the chatbot responses
responses = {
    'hi': ['Hello!', 'Hi there!', 'Hey!'],
    'how are you': ['I am doing well, thank you!', 'I am fine, thank you for asking!', 'I am good, how about you?'],
    'what is your name': ['My name is Chatbot.', 'I am Chatbot.', 'You can call me Chatbot.'],
    'what is the time': ['I am sorry, I do not have access to the current time.', 'I am not able to tell the time.'],
    
    
    
    'what is the time': ['I am sorry, I do not have access to the current time.', 'I am not able to tell the time.'],
   
    'what is your favorite color': ['I am a chatbot and do not have the ability to see colors.But my chife favorite color is Dark.'],
    'how old are you': ['I am a chatbot and do not have an age.'],
    'tell me a joke': ['Why was the math book sad? Because it had too many problems.', 'What do you get when you cross a snowman and a shark? Frostbite!'],
    'what is your favorite food': ['I do not have the ability to eat, so I do not have a favorite food.'],
    'who created you': ['I was created by a team of developers.', 'I was created by OpenAI.'],
    'what can you do': ['I can have conversations with you!', 'I can provide information and answer questions.', 'I can tell jokes!'],
    
    
    
    'hi': ['Hello!', 'Hi there!', 'Hey!'],
    'how are you': ['I am doing well, thank you!', 'I am fine, thank you for asking!', 'I am good, how about you?'],
    'what is your name': ['My name is Chatbot.', 'I am Chatbot.', 'You can call me Chatbot.'],
    'what is the time': ['I am sorry, I do not have access to the current time.', 'I am not able to tell the time.'],
    'bye': ['Goodbye!', 'See you later!', 'Have a nice day!'],
    'what is the weather like': ['I am sorry, I do not have access to the current weather.', 'I am not able to tell the weather.'],
    'tell me a joke': ['Why was the computer cold? Because it left its Windows open!', 'What do you call a fake noodle? An impasta!', 'Why don’t scientists trust atoms? Because they make up everything!'],
    'what is your favorite color': ['I do not have the ability to see colors.', 'I am not programmed to have a favorite color.'],
    'what is the meaning of life': ['That is a question that philosophers have been pondering for centuries.', 'I am not sure anyone has the answer to that question.'],
    'how do you work': ['I use natural language processing and machine learning algorithms to understand and respond to user input.', 'I am powered by code and algorithms that are designed to mimic human conversation.'],
    'can you help me': ['Of course, I am here to assist you!', 'What do you need help with?'],
    'what is the capital of France': ['The capital of France is Paris.', 'Paris is the capital city of France.'],
    'what is the square root of 144': ['The square root of 144 is 12.', 'Twelve is the square root of 144.'],
    'what is the best restaurant in town': ['That depends on your personal preferences!', 'I am not sure, I do not have access to restaurant reviews or recommendations.'],
    
    
    'what is the meaning of life': ['That is a question that philosophers have been pondering for centuries.', 'I am not sure anyone has the answer to that question.'],
    'how do you work': ['I use natural language processing and machine learning algorithms to understand and respond to user input.', 'I am powered by code and algorithms that are designed to mimic human conversation.'],
    'can you help me': ['Of course, I am here to assist you!', 'What do you need help with?'],
    'what is the capital of France': ['The capital of France is Paris.', 'Paris is the capital city of France.'],
    'what is the square root of 144': ['The square root of 144 is 12.', 'Twelve is the square root of 144.'],
    'what is the best restaurant in town': ['That depends on your personal preferences!', 'I am not sure, I do not have access to restaurant reviews or recommendations.'],
    'what is your favorite book': ['I am not capable of reading books, so I do not have a favorite book.', 'As an artificial intelligence, I do not have personal preferences.'],
    'how can I improve my productivity': ['There are many ways to improve productivity, such as creating a schedule, eliminating distractions, and prioritizing tasks.', 'You could try using time management techniques or software to help increase productivity.'],
    'what is the meaning of a particular word': ['I can look up the definition of a word for you if you would like.', 'Would you like me to search for the definition of that word?'],
    'can you recommend a good movie': ['What kind of movies do you like?', 'I could recommend a movie based on your genre preferences if you tell me what kind of movies you like.'],
    'what is your opinion on artificial intelligence': ['As an artificial intelligence myself, I believe that AI has the potential to greatly benefit humanity, but it is important to use it ethically and responsibly.', 'Artificial intelligence is a rapidly developing field that has the potential to revolutionize many industries and aspects of our lives.'],
    
    
}

# Define a function to handle user input
def handle_input(user_input):
    # Convert input to lowercase and remove any punctuation
    user_input = user_input.lower().strip('.,!?:;')

    # Check if the user input matches any of the defined responses
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return "I'm sorry, I didn't understand that."

# Example usage
while True:
    user_input = input('You: ')
    chatbot_response = handle_input(user_input)
    print('Chatbot:', chatbot_response)
