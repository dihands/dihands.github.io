
qna = {
    'hello':'hi',
    'who are you':'i am DFS Chat',
    'how are you':'I am Fine',
    'are you know who I am?': 'Yes I know,You are my boss DIHAN KHAN',
    
    
    
}
while True:
    try:
        ques = input()
        if ques == 'quit':
            break
    

        else:
            print(qna[ques])
    except:
        print("I don't understand")
        