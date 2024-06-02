print("ENTER ID : ")

qna = {
    'DS2034FFD4':'ENTER PASSWORD : ',
    '12DT508DS':'Login success:THE INFORMATION IS[MY NAME IS DIHAN KHAN]',
    
    
    
    
}
while True:
    try:
        ques = input()
        if ques == 'quit':
            break
    

        else:
            print(qna[ques])
    except:
        print("ID & PASSWORD IS WRONG.TRY AGAIN")