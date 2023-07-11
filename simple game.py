print("Hello, welcome to my quiz!")
ans=input('Are you ready to play? (yes/no):')
score=0
total_q=4
if ans.lower()=='yes':
    ans=input('1. What is my name? ')
    if ans.lower()=='lidija':
        score+=1
        print('Correct!')
    else:
        print('Incorrect!')
        
    ans=input('2. Where am I from? ')
    if ans.lower()=='serbia':
        score+=1
        print('Correct!')
    else:
        print('Incorrect!')
        
    ans=input('3. How old am I? ')
    if ans=='41':
        score+=1
        print('Correct!')
    else:
        print('Incorrect!')
        
    ans=input('4. Which instrument do I play? ')
    if ans.lower()=='piano' or ans.lower()=='harpichord' or ans.lower()=='flute':
        score+=1
        print('Correct!')
    else:
        print('Incorrect!')
        
    ans=input('5. Who are you? ')
    if ans.lower()==('johannes'):
        score+=1
        print('Correct!')
    else:
        print('Incorrect!')
        
    ans=input('6. Where do you live? ')
    if ans.lower()==('netherlands'):
        score+=1
        print('Correct!')
    else:
        print('Incorrect!')

    print('Thank you for playing, you got', score, "questions correct.")
    mark=(score/total_q)*100
    print("Mark", str(mark)+'%')
print('Goodbye')

        

        
        