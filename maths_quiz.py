#Write the python code for the game appilication and name it as Maths_Quiz
#In that there will be the random questions for every correct answer there will be +5 marks and for every worng answer there will be -2 marks have to be allowed
#Use the time function that how much time does the gamer will take for complesion the task
#update the score for correct answer +5 marks and for wrong answer -2 marks


import time         #importing the time function
import random       #importing random function
begin=time.time()   #starting time
score=0
print("Maths_Quiz")
def game():      #user defined function and naming it as game
    global score
    choice=random.randint(1,4)
    #choosing the random number from 1 to 4
    
    if choice==1:
    #If the choosing number is 1 by the choice then the block of code will be executed
        a=random.randint(0,9) 
        b=random.randint(0,9)
        #choosing a random number form 0 to 9 by "a" and "b" variables
        c=a*b
        #caliculating the answer
        print(a,"*",b,"=","_?_")
        #displaying the question
        d=int(input("Enter your answer:"))
        #asking the question by the compiler
        if c==d:
            #displaying whether the answer is correct or wrong
            print("Correct answer:")
            score+=5  
            #incrementing the result for the correct one is +5
        else:
            print("Wrong answer:")
            print("The correct answer is:",c)
            score-=2
            #Decrementing the result for the wrong answer as -2
            
    elif choice==2:
        #If the choice choosing will be 2 randomly then the block of code will be executed
        a=random.randint(0,9)
        b=random.randint(0,9)
        c=a+b
        print(a,"+",b,"=","_?_")
        #displaying the question to the gamer
        d=int(input("Enter your answer:"))
        #asking the answer form the gamer
        
        if c==d:
            print("correct answer:")
            score+=5
            #incrementing the score as +5 for the correct one
        else:
            print("Wrong answer")
            print("The correct answer is:",c)
            #displaying the wrong answer
            score-=2
            #decrementing the score as -2
            
    elif choice==3:
        #If the choice chooses the random number as 3 then the block of code will be executed
        a=random.randint(0,9)
        b=random.randint(0,9)
        c=a-b
        print(a,"-",b,"=","_?_")
        #displaying the question for the gamer
        d=int(input("Enter your answer:"))
        #expecting the answer form the gamer
        if c==d:
            print("Correct answer:")
            #For every correct answer the score incremented to +5
            score+=5
        else:
            print("Wrong answer:")
            print("The correct answer is:",c)
            #displaying the correct answer if the answer is wrong
            score-=2
            #the score will be decremented for -2
            
    elif choice==4:
        #The block of code will executed if the random number will be 4
        a=random.randint(0,9)
        b=random.randint(0,9)
        c=a/b
        print(a,"/",b,"=","_?_")
        #displaying the question for the gamer
        d=int(input("Enter your answer:"))
        #Asking the answer from the gamer
        
        if c==d:
            print("Correct answer")
            score+=5
            #for correct answer incrementing the score for +5
            
        else:
            print("Wrong answer")
            print("The correct answer is:",c)
            #displaying the correct answer if the answer is wrong
            score-=2
            #decrementing the score for -2 if the answer is wrong
for i in range(10):
    game()
    #The game function will be run for 10 times and asks 10 questions from the gamer
    
time.sleep(1)
end=time.time()
#The total time taken by the user for attempting the answers

print("Total time taken:",end-begin,"seconds")
#displaying the total time taken by the gamer

print("Total score:",score)
#displaying the score to the gamer by the compiler

if score>=45:
    #score greater than 45 then the block of code will be executed
    print("Outstanding!!")
    
elif score>=40:
    #score greater than 40 then the block of code will be executed
    print("Exceeds Expectations!!")
    
elif score>=30:
    #score greater than 30 then the block of code will be executed
    print("Meets Expectations!!")
    
elif score>=20:
    #score greater than the block of code will be executed
    print("Needs Improvement!!")
    
elif score>=10:
    #score greated then 10 then the block of code will be executed
    print("Needs More Improvenent!!")
    
else:
    #It will be the default message
    print("Unacceptable")
    
print("GAME_Over")
#printing theat the game is compleated