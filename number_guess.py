import random
top_range = input('Type a number:' )

if top_range.isdigit():
    top_range = int(top_range)
    if top_range <=0:
        print ('Please type a number larger than 0 next time')
        quit()
else:
    print ('Please type a number next time')
    quit()

random_num = random.randint(0, top_range)
guesses= 0


while True:
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
        guesses +=1
    else:
        print ('Please type a number next time')
        continue
    if user_guess == random_num:
       
        break
    elif user_guess > random_num:
            print('You were above the number!')
            
    else:
            print('You were below the number!')
    continue
print('Correct! You got it in ' + str(guesses) +  ' ' +'guesses!')