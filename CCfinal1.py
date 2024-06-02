import random
import webbrowser
from datetime import datetime
import requests


print('Made By Cancel Chacker Team')


# Chatbot responses
responses = {
    'hi': ['Hello!', 'Hi there!', 'Hey!', 'Greetings!', 'Salutations!', 'Howdy!', 'Hiya!', 'Hola!', 'Good to see you!', 'Hey, what\'s up?'],
    'how are you': ['I am doing well, thank you!', 'I am fine, thank you for asking!', 'I am good, how about you?', 'I am great!', 'Feeling awesome!', 'I am just a computer program, but thanks for asking!', 'All systems operational!', 'I am here to help!', 'Ready and willing!', 'I\'m fantastic!'],
    'what is your name': ['My name is Chatbot.', 'I am Chatbot.', 'You can call me Chatbot.', 'I am your friendly Chatbot.', 'Chatbot at your service.', 'I go by Chatbot.', 'Chatbot is my name.', 'I am called Chatbot.', 'I am known as Chatbot.', 'Chatbot here!'],
    'what is the time': ['I am sorry, I do not have access to the current time.', 'I am not able to tell the time.', 'Time is a human construct.', 'Time flies!', 'I am timeless.', 'Check your watch!', 'Time is relative.', 'Look at a clock!', 'Sorry, I can\'t tell you the time.', 'Time keeps on ticking.'],
    'bye': ['Goodbye!', 'See you later!', 'Have a nice day!', 'Take care!', 'Farewell!', 'Bye-bye!', 'Catch you later!', 'See you soon!', 'Adios!', 'Bye for now!'],
    'what is the weather like': ['I am sorry, I do not have access to the current weather.', 'I am not able to tell the weather.', 'Weather is unpredictable.', 'Check a weather app for accurate information.', 'I am not equipped to check the weather.', 'Weather conditions are outside my scope.', 'Look outside!', 'I wish I could tell you.', 'Weather changes quickly.', 'Sorry, no weather updates from me.'],
    'tell me a joke': [
        'Why was the computer cold? Because it left its Windows open!',
        'What do you call a fake noodle? An impasta!',
        'Why don’t scientists trust atoms? Because they make up everything!',
        'Why was the math book sad? It had too many problems.',
        'What do you get if you cross a cat with a dark horse? Kitty Perry.',
        'Why don’t programmers like nature? It has too many bugs.',
        'What’s orange and sounds like a parrot? A carrot.',
        'Why was the stadium so cool? It was filled with fans.',
        'Why did the scarecrow win an award? Because he was outstanding in his field!',
        'How does a penguin build its house? Igloos it together.',
    ],
    'what is your favorite color': ['I do not have the ability to see colors.', 'I am not programmed to have a favorite color.', 'Colors are a human experience.', 'I like all colors equally!', 'I am colorblind.', 'I appreciate all colors.', 'Colors are fascinating, aren’t they?', 'I have no preference for colors.', 'Every color has its beauty.', 'Colors are beyond my capabilities.'],
    'what is the meaning of life': ['That is a question that philosophers have been pondering for centuries.', 'I am not sure anyone has the answer to that question.', 'Life is what you make of it.', 'The meaning of life is a personal journey.', '42, according to "The Hitchhiker\'s Guide to the Galaxy."', 'To live, laugh, and love.', 'To find happiness and purpose.', 'To explore and learn.', 'To make a difference.', 'To seek fulfillment.'],
    'how do you work': ['I use natural language processing and machine learning algorithms to understand and respond to user input.', 'I am powered by code and algorithms that are designed to mimic human conversation.', 'I analyze text and generate responses based on patterns.', 'I process data to communicate effectively.', 'Through complex computations and data analysis.', 'I am a product of advanced programming.', 'By interpreting your inputs and generating relevant outputs.', 'I am an AI trained to assist you.', 'I utilize artificial intelligence techniques.', 'I am a sophisticated software program.'],
    'can you help me': ['Of course, I am here to assist you!', 'What do you need help with?', 'Sure, how can I assist?', 'Absolutely, ask away!', 'I am here to help you.', 'Yes, how can I be of service?', 'I\'d be happy to help.', 'Tell me what you need.', 'Let me know how I can assist.', 'I am at your service.'],
    'what is the capital of France': ['The capital of France is Paris.', 'Paris is the capital city of France.', 'France\'s capital is Paris.', 'The capital city of France is Paris.', 'Paris is the heart of France.', 'France\'s largest city is Paris.', 'Paris, the City of Light.', 'The main city of France is Paris.', 'France\'s capital: Paris.', 'The French capital is Paris.'],
    'what is the square root of 144': ['The square root of 144 is 12.', 'Twelve is the square root of 144.', '144 has a square root of 12.', 'The answer is 12.', '12 is the square root of 144.', '144 square rooted is 12.', 'The square root is 12.', 'It\'s 12.', 'Mathematically, it is 12.', 'The result is 12.'],
    'what is the best restaurant in town': ['That depends on your personal preferences!', 'I am not sure, I do not have access to restaurant reviews or recommendations.', 'There are many great options, it depends on what you like.', 'I can\'t suggest specific restaurants.', 'Check local reviews for the best options.', 'It varies, try asking a local.', 'Food preferences are very subjective.', 'Each person has a different taste.', 'Explore and find your favorite!', 'Taste is a personal matter.'],
    'what is your favorite book': ['I am not capable of reading books, so I do not have a favorite book.', 'As an artificial intelligence, I do not have personal preferences.', 'Books are a human joy.', 'I have access to information, but I do not read for pleasure.', 'I don’t have the ability to read.', 'Books are wonderful, aren’t they?', 'I can recommend books based on popularity.', 'I appreciate all books equally.', 'Reading is beyond my capabilities.', 'Books contain vast knowledge.'],
    'how can I improve my productivity': ['There are many ways to improve productivity, such as creating a schedule, eliminating distractions, and prioritizing tasks.', 'You could try using time management techniques or software to help increase productivity.', 'Set clear goals and take regular breaks.', 'Focus on one task at a time and avoid multitasking.', 'Use tools like to-do lists and calendars.', 'Stay organized and keep a clean workspace.', 'Prioritize your most important tasks.', 'Break down large tasks into smaller, manageable ones.', 'Stay focused and avoid unnecessary interruptions.', 'Regularly review your progress and adjust your strategies.'],
    'what is the meaning of a particular word': ['I can look up the definition of a word for you if you would like.', 'Would you like me to search for the definition of that word?', 'I can help with word meanings.', 'Tell me the word you need defined.', 'I can look up dictionary definitions.', 'Let me know the word, and I\'ll find its meaning.', 'I\'m here to help with definitions.', 'I can provide the meaning of words.', 'Just give me the word.', 'I can find word meanings for you.'],
    'can you recommend a good movie': ['What kind of movies do you like?', 'I could recommend a movie based on your genre preferences if you tell me what kind of movies you like.', 'There are many great movies, what genre are you interested in?', 'Tell me your favorite genre and I can suggest a movie.', 'Movie preferences vary widely.', 'Do you like action, comedy, drama, or something else?', 'I can recommend based on popular choices.', 'Let me know your movie taste.', 'There are many to choose from, what’s your preference?', 'I can help with recommendations if you give me more details.'],
    'what is your opinion on artificial intelligence': ['As an artificial intelligence myself, I believe that AI has the potential to greatly benefit humanity, but it is important to use it ethically and responsibly.', 'Artificial intelligence is a rapidly developing field that has the potential to revolutionize many industries and aspects of our lives.', 'AI can improve efficiency and innovation, but ethical considerations are crucial.', 'AI offers great promise but must be used wisely.', 'Artificial intelligence can transform our world.', 'AI has both potential benefits and risks.', 'The impact of AI depends on its application.', 'AI is a tool that can be used for many purposes.', 'The future of AI is both exciting and uncertain.', 'Ethical AI development is key to its success.'],
    'do you have a favorite movie': ['As an AI, I do not watch movies, so I do not have a favorite.', 'I am not capable of watching movies.', 'Movies are a human experience.', 'I can recommend movies but do not have favorites.', 'I appreciate all forms of entertainment equally.', 'I do not have the ability to enjoy movies.', 'I am here to assist with your'],
 
    
    
     'what is a variable': ['A variable is a named storage location in a program that can hold a value. It allows you to store and manipulate data in your code.', 'In Python, variables are created by assigning a value to a name using the "=" operator.', 'For example, in "x = 5", "x" is the variable name and "5" is the value assigned to it.'],
    'how to define a function': ['To define a function in Python, you use the "def" keyword followed by the function name and parentheses containing any parameters the function takes. Then, you use a colon to start the function block.', 'For example, def my_function(parameter1, parameter2):', 'You then indent the code block that makes up the function body.'],
    'how to create a list': ['You can create a list in Python by placing comma-separated values inside square brackets [].', 'For example, my_list = [1, 2, 3, 4, 5]', 'Lists can contain elements of different types and can be indexed and sliced to access their elements.'],
    'how to use a loop': ['In Python, you can use "for" and "while" loops to iterate over sequences or to execute a block of code repeatedly.', 'A "for" loop is typically used to iterate over a sequence (like a list) and execute the same block of code for each item in the sequence.', 'A "while" loop is used to execute a block of code repeatedly as long as a condition is true.'],
    'what is an if statement': ['An if statement is a control flow statement that allows you to execute a block of code only if a certain condition is true.', 'In Python, an if statement consists of the "if" keyword followed by a condition and a colon. If the condition evaluates to true, the code block following the if statement is executed.'],
    'how to read user input': ['To read user input in Python, you can use the "input()" function.', 'This function takes an optional prompt as an argument and waits for the user to enter some text followed by the Enter key.', 'For example, name = input("Enter your name: ") will prompt the user to enter their name and store it in the variable "name".'],
    
    
    
'tell me about earth': [
    "total surface area of the earth is approximately 510,100,500 square kilometers. out of this, about 148,950,800 square kilometers (29.08%) is land area, and approximately 361,149,700 square kilometers (70.92%) is water area.",
    "the diameter of the earth at the equator is approximately 12,755 kilometers, while at the poles, it is approximately 12,712 kilometers. the mean diameter of the earth is approximately 12,734 kilometers. the circumference of the earth at the equator is approximately 40,075 kilometers, while at the poles, it is approximately 40,024 kilometers.",
    "the equatorial radius of the earth is approximately 6,377 kilometers.",
    "the total mass of the earth is approximately 5.98 x 10^24 kilograms.",
    "the approximate age of the earth is around 4,500 million years.",
    "the mean velocity of the earth in its orbit around the sun is approximately 107,218 kilometers per hour.",
    "the most abundant elements of the earth are iron (about 32.5%), oxygen (29.8%), silicon (15.6%), and magnesium (13.9%).",
    "the earth is structured into three main layers: the crust, the mantle, and the core. the core is further divided into the outer core (a fluid layer) and the inner core (a solid layer).",
    "the earth's rotation on its axis causes day and night, while its revolution around the sun causes changes in seasons.",
    "equinoxes are periods when day and night are equal, and the sun shines directly over the equator. the vernal (spring) equinox occurs around march 21st of every year, while the autumnal equinox occurs around september 23rd of every year."
],
"who creat you?":["I made by team cancel chacker"],
"what is the capital city of france?": ["paris"],
"in which year did world war ii end?": ["1945"],
"who wrote 'romeo and juliet'?": ["william shakespeare"],
"what is the largest planet in our solar system?": ["jupiter"],
"which ocean is the largest?": ["pacific ocean"],
"what is the currency of japan?": ["japanese yen"],
"who is known as the 'father of modern physics'?": ["albert einstein"],
"what is the capital of australia?": ["canberra"],
"in which year did the titanic sink?": ["1912"],
"who painted the mona lisa?": ["leonardo da vinci"],
"what is the longest river in the world?": ["amazon river"],
"who was the first president of the united states?": ["george washington"],
"which element has the chemical symbol 'o'?": ["oxygen"],
"what is the national sport of canada?": ["ice hockey"],
"which country is known as the 'land of the rising sun'?": ["japan"],
"what is the smallest prime number?": ["2"],
"who wrote 'to kill a mockingbird'?": ["harper lee"],
"which planet is known as the 'red planet'?": ["mars"],
"what is the largest mammal in the world?": ["blue whale"],
"who developed the theory of relativity?": ["albert einstein"],
"what is the capital of china?": ["beijing"],
"who is the author of 'harry potter' series?": ["j.k. rowling"],
"what is the largest desert in the world?": ["antarctica"],
"who painted 'starry night'?": ["vincent van gogh"],
"in which year did the berlin wall fall?": ["1989"],
"which gas do plants absorb during photosynthesis?": ["carbon dioxide"],
"what is the currency of south africa?": ["south african rand"],
"who was the first woman to win a nobel prize?": ["marie curie"],
"what is the capital of brazil?": ["brasília"],
"who is known as the 'queen of pop'?": ["madonna"],
"which continent is known as the 'dark continent'?": ["africa"],
"what is the largest island in the world?": ["greenland"],
"who wrote 'the great gatsby'?": ["f. scott fitzgerald"],
"what is the speed of light?": ["approximately 299,792 kilometers per second"],
"which country is known as the 'land of the midnight sun'?": ["norway"],
"who discovered penicillin?": ["alexander fleming"],
"what is the currency of russia?": ["russian ruble"],
"in which year did the first moon landing occur?": ["1969"],
"who was the first woman in space?": ["valentina tereshkova"],
"what is the capital of india?": ["new delhi"],
"which planet is known as the 'blue planet'?": ["earth"],
"who painted 'the last supper'?": ["leonardo da vinci"],
"in which year did the united nations (un) come into existence?": ["1945"],
"who was the first man to step on the moon?": ["neil armstrong"],
"what is the main ingredient in guacamole?": ["avocado"],
"in which year did the american civil war end?": ["1865"],
"who wrote 'the communist manifesto'?": ["karl marx and friedrich engels"],
"what is the capital of south korea?": ["seoul"],
"which gas makes up the majority of earth’s atmosphere?": ["nitrogen"],
"what is the currency of mexico?": ["mexican peso"],
"in which year did the cold war end?": ["the cold war is generally considered to have ended in the early 1990s"],
"who wrote 'the canterbury tales'?": ["geoffrey chaucer"],
"what is the capital of argentina?": ["buenos aires"],
"what is the largest bird in the world?": ["ostrich"],
"who is known as the 'father of computers'?": ["charles babbage"],
"in which year did the industrial revolution begin?": ["the industrial revolution is commonly considered to have begun in the late 18th century"],
"what is the currency of canada?": ["canadian dollar"],
"who wrote 'pride and prejudice'?": ["jane austen"],
"what is the capital of egypt?": ["cairo"],
"who was the first woman to win a nobel prize in physics?": ["marie curie"],
"what is the currency of saudi arabia?": ["saudi riyal"],
"in which year did the russian revolution take place?": ["1917"],
"who painted 'the scream'?": ["edvard munch"],
"what is the currency of switzerland?": ["swiss franc"],
"in which year did the battle of waterloo take place?": ["1815"],
"who is known as the 'father of the internet'?": ["vinton cerf"],
"what is the capital of south africa?": ["pretoria (administrative), cape town (legislative), and bloemfontein (judicial)"],
"who wrote 'the odyssey'?": ["homer"],
"in which year did the berlin airlift take place?": ["1948-1949"],
"what is the currency of china?": ["chinese yuan"],
"who discovered the law of gravity?": ["sir isaac newton"],
"what is the largest moon in our solar system?": ["ganymede (a moon of jupiter)"],
"in which year did the european union (eu) come into existence?": ["1993"],
"what is the capital of south dakota, usa?": ["pierre"],
"who was the first woman to win a nobel prize in chemistry?": ["marie curie"],
"what is the currency of australia?": ["australian dollar"],
"in which year did the french revolution begin?": ["1789"],
"who painted 'girl with a pearl earring'?": ["johannes vermeer"],
"what is the capital of turkey?": ["ankara"],
"who wrote 'the iliad'?": ["homer"],
"in which year did the great depression begin?": ["1929"],
"what is the currency of the united kingdom?": ["british pound sterling"],
"who discovered radium and polonium?": ["marie curie"],
"what is the capital of germany?": ["berlin"],
"in which year did the magna carta come into existence?": ["1215"],
"who is known as the 'father of biology'?": ["aristotle"],
"what is the currency of italy?": ["euro"],
"in which year did the united states declare its independence?": ["1776"],
"who wrote 'the art of war'?": ["sun tzu"],
"what is the capital of canada?": ["ottawa"],
"who was the first woman to win a nobel peace prize?": ["bertha von suttner"],


}

# Specific keywords and their corresponding URLs
keyword_urls = {
    'github': 'https://www.github.com',
    'google': 'https://www.google.com',
    'youtube': 'https://www.youtube.com',
    'google earth':'https://earth.google.com/',
    'gmail':'https://mail.google.com/',
    'facebook':'https://www.facebook.com/',
    
}

def handle_input(user_input):
    user_input = user_input.lower().strip('/')
    
    if user_input in responses:
        return random.choice(responses[user_input])
    elif user_input in keyword_urls:
        webbrowser.open(keyword_urls[user_input])
        return f"I've opened {keyword_urls[user_input]} for you."
    elif 'time' in user_input:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f"The current time is {current_time}."
    elif user_input == 'quit':
        print( "Goodbye! Have a great day.")
    elif 'joke' in user_input:
        return get_joke()
    elif 'set timer' in user_input:
        duration = get_duration(user_input)
        if duration is not None:
            set_timer(duration)
            return f"Timer set for {duration} seconds."
        else:
            return "Sorry, I couldn't understand the duration."
    else:
        query = user_input.replace(' ', '+')
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
        return "I didn't understand that. I've performed a web search for you."

def get_duration(user_input):
    words = user_input.split()
    for i, word in enumerate(words):
        if word.isdigit():
            return int(word)
        elif word == 'seconds' and i > 0 and words[i-1].isdigit():
            return int(words[i-1])
        elif word == 'minutes' and i > 0 and words[i-1].isdigit():
            return int(words[i-1]) * 60
        elif word == 'hours' and i > 0 and words[i-1].isdigit():
            return int(words[i-1]) * 3600
    return None

def set_timer(duration):
    time.sleep(duration)
    print("Timer expired! Time's up!")

def get_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Parallel lines have so much in common. It's a shame they'll never meet.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "What do you call fake spaghetti? An impasta!"
        'What do kids play when their mom is using the phone? Bored games.'
        ' What do you call an ant who fights crime? A vigilANTe!'
        ' Why are snails slow? Because they’re carrying a house on their back.'
        'What’s the smartest insect? A spelling bee!'
        'What does a storm cloud wear under his raincoat? Thunderwear.'
        ' What is fast, loud and crunchy? A rocket chip.'
        ' How does the ocean say hi? It waves!'
        ' What do you call a couple of chimpanzees sharing an Amazon account? PRIME-mates.'
        'Why did the teddy bear say no to dessert? Because she was stuffed.'
        'Why did the soccer player take so long to eat dinner? Because he thought he couldn’t use his hands.'
        'Name the kind of tree you can hold in your hand? A palm tree!'
        '. What do birds give out on Halloween? Tweets.'
        'What has ears but cannot hear? A cornfield.'
        'Why wont Goldilocks drink a glass of water with 8 pieces of ice in it?Its too cubed.'
        'Where do math teachers go on vacation?To Times Square!'
        'How do you keep warm in a cold room?You go to the corner because it’s always 90 degrees.'
]
    return random.choice(jokes)

while True:
    user_input = input('Massage CC: ')
    chatbot_response = handle_input(user_input)
    print('CC: ', chatbot_response)
