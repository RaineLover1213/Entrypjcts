# Welcome User to your quiz
print('Welcome to the classics quiz!')
# Ask user if they are ready to play
playing = input('Are you rady to play (Y/N)?').lower()
# If user doesnt type yes end program

if playing != 'y'.lower():
    quit()
print('Lets get started!')
answer = input('Where did the book "Tale of two cities" take place? ').lower()
score = 0
if answer == 'paris'.lower():
    print('Correct!')
    score +=1
else:
    print('IncorrecT!')
answer = input('In the book the giver, who was the reciever of memory? ').lower()
if answer == 'jonas'.lower():
    print('Correct!')
    score +=1
else:
    print('IncorrecT!')
answer = input('Who is the author of "The count of monte cristo"? ').lower()
if answer == 'dumas'.lower():
    print('Correct!')
    score +=1
else:
    print('IncorrecT!')
answer = input('What vampire book did Bram Stoker write? ').lower()
if answer == 'dracula'.lower():
    print('Correct!')
    score +=1
else:
    print('IncorrecT!')
answer = input('Who is the protagonist in "The catcher in the rye"? ').lower()
if answer == 'holden caulfield'.lower():
    print('Correct!')
    score +=1
else:
    print('Incorrect!')
print('you got ' + str(score) +  ' ' + 'Questions correct')
print('you got ' + str((score / 4) * 100) +'%.')


           
#



    
    

    
       
    
    
    

