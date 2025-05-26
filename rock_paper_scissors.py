import random
# Two variable for user score and cpu score
user_score = 0
cpu_score = 0


options = ['rock', 'paper', 'scissors']


while True:
    user_input = input('Type rock/paper/scissors to play, q to quit: ').lower()
    if user_input == 'q':
        break
    if user_input not in options:
        print('INVALID')
        continue
    random_num = random.randint(0, 2)
    cpu_pick = options[random_num]
    print('CPU picked', cpu_pick + '.')

    if user_input == 'rock' and cpu_pick == 'scissors'.lower():
      print('YOU WIN!')
      user_score += 1
    elif user_input == 'paper' and cpu_pick == 'rock'.lower():
      print('YOU WIN!')
      user_score += 1
    elif user_input == 'scissors' and cpu_pick == 'paper'.lower():
      print('YOU WIN!')
      user_score += 1
    elif user_input == options and  cpu_pick == options:
      print('YOU TIED!')
    
      
    else:
      print('YOU LOSE!')
      cpu_score += 1
    
    
#  Rock = 0 paper = 1 scissors = 2

    
    
    
print('USER SCORE:', user_score)
print('CPU SCORE:', cpu_score)    
print('GOODBYE')         
    
    