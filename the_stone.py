import time
name = input ("What is your name? ")
print ('Hello,',  name, 'welcome to a game where you choose your own path!')

answer = input(
    ' You must set off from your family, which mode of travel will you choose, by horse or by boat? ').lower()

if answer == 'horse':
    print('Ah, you chose the trusty steed, a fine choice')
    answer = input(
        "As you are riding your horse you see a distressed maiden, will you stop to help her, yes or no? ").lower()
    if answer == 'yes':
        print('You come to the maidens aid like a true knight and she offers you to come with her, will you accept of refuse?')
        answer = input('accept or refuse? ').lower()
        if answer == 'accept':
            print('You follow to the maiden to a nearby cave where she offers you a incandescent stone of wonder, what will you do?')
            answer = input('Take or leave? ').lower()
            if answer == 'take':
                print('As you pick the stone up you are invigorated by a power unknown to man, you feel how you imagine the gods feel.')
                answer = input('After you feel the power enter you, the stone teleports you to an island and you see people in the sistance, will you approach or hide? ').lower()
                if answer == 'approach':
                    print('You approach the band of pirates and they all look in astonishment at you because you look identical to a man in their crew.')
                    answer = input('The one who looks like you asks your name, will you give them your name or no? ').lower()
                    if answer == name:
                        print(f'They all gasp and the person who looks like you says "My name is {name}"')
                        print('You realize who has been talking to you is your own self, at this realization the stone glows red and creates a explosion so vast it destroys the whole planet, YOU DIED TWICE')
                    if answer == 'no':
                        print('The captain of the crew shoots you in the face with a blunderbuss before you can say a word, YOU DIED')    
                if answer == 'hide':
                    print('You run and hide in some bush and a venomous komado dragon bites and poisions you.')
                    answer = input('The pain is severe the pirates hear your screams and come runnning towards you, will you plead for help, or try to run')
                    if answer == 'plead':
                        print('The pirates agree to help you but all of a sudden your heart stops, YOU DIED')
                    if answer == 'run':
                        print('You try to run but one pirate shoots you in the back, YOU DIED')    
                
            if answer == 'leave':
                print('The maiden screams as a greatsword weilding bandit enters the cave with eyes on the stone')
                answer = input('will you protect the maiden or flee? ').lower()
                if answer == 'flee':
                    print(' You escape with your life but the dying maidens screams torment you')
                    answer = input('Will you camp out for the night or will you search for food? ').lower()
                    if answer == 'camp':
                        print('As you are searching for wood to build a campfire you hear a villainous laugh.')
                        answer = input('Shall you investigate are continue the search for wood? ').lower()
                        if answer == 'investigate':
                            print('It is the maiden, bloody and ravenous, she compels you to chase her with her laughs, youre led to a ravine where she dissapears as you fall trying to grab her. YOU DIED')
                        if answer == 'continue':
                            print('You find wood but as you sleep youre assasinated by the bandit that kiled the maiden. YOU DIED')    
                    if answer =='food':
                        print('You find some berries already sat out on a rock')
                        answer = input('Will you eat or pass up on the berries? ').lower()
                        if answer == 'eat':
                            print('The berries taste so good but ass you finish the last one you become delirous and lose functionality of your senses. YOU DIED')
                            
                        if answer == 'pass':
                            print('You pass up on the berrries but youre so weak from lack of food and water you go back to get the berries but a bear awaits you and ambushes you. YOU DIED')    
                
                
                if answer == 'protect':
                    print('The bandit disarms you of your dagger with swiftness and fells you, your bravery gave the maiden time to flee. YOU DIED')    
               
        
        
        if answer == 'refuse':
            print('The maiden wishes you well and gives you the dagger she had, saying she had no use of it anymore.')
            answer = input(
                'Before you get back on your horse, a bear come from the brush, heading straigt for you, will you fight or flee? ').lower()
            if answer =='fight':
                print('With the dagger you wrestle with the bear before felling it with a pierce through its heart. well done.')
                answer = input(
                    ' Your horse has since ran away, will you search for shelter or food? ').lower()
                if answer == 'shelter':
                    print('You come to a cave and find the maiden you mets body bludgeoned and in her hand is a incandescent stone of wonder, what will you do?')
                    answer = input('Take or leave? ').lower()
                    if answer == 'take':
                        print('You feel a surged of power surged through you but you also hear the maidens cries, condemming you for leaving her to die, the stone glows red and you feel your skin melting off. seconds later.....YOU DIED')
                        if answer == 'leave':
                            print('As you go to leave, a bandit strikes you from behind with a longsword. YOU DIED.')
                    
                
                
                if answer == 'food':
                    print('You find a ravine that has a spring near it and a berry bush.')
                    answer = input('Will you drink or eat? ').lower()
                    if answer =='eat':
                        print('The berries taste sour and instantly you feel your heart stop. YOU DIED')
                if answer == 'drink':
                    print('You get your fill and feel replinished, you see a hermitage acrossed the spring.')
                    answer = input('Will you cross the spring or go around it? ').lower() 
                    if answer =='cross':
                        print('You successfully cross to the hermitage, you knock on the door and are denied entry, the hermit tell you that you arent a knight of god.')
                        answer = input("Will you disregard the hermit and help yourself to his alms or will you go on your way? ").lower() 
                        if answer == 'disregard':
                            print(' the hermit does nothing but prays and crosses himself, you help yourself to some bread and water then leave.')
                            answer = input('Will you set up camp or explore more? ').lower()
                        if answer == 'go':
                            print('The hermit throws some bread out to you, you thank him and go on your way.') 
                            answer = input("Will you set up camp or continue exploring? ").lower()
                            if answer == 'explore':
                                print(' you find a abandoned cabin, but as you pass the door to go inside you step on a pressure plate, sending spikes through your whole body. YOU DIED')
                            if answer == 'camp':
                               print('you set up camp but the rain dispels your fire, thunder strikes you and....YOU DIED ')       
                        
                    if answer == 'go around':
                        print('You go around it but slip on the edge of the ravine and fall to oblivion. YOU DIED')          
                
            if answer == 'flee':
                print('You try to flee but the bear makes easy work of catching and devouring you, YOU DIED.')
                
    if answer == 'no':
        print('You keep riding, and the your horse gets startled by wolves and throws you off, luckily, there is a abandoned carriage near, will you run for the carriage are try to get back on horse? ')
        answer = input('run or ride? ').lower()
        if answer == 'run':
            print('You reach the carriage where inside you find a blunderbuss and a battle axe.')
            answer = input('Will you fight the wolves or wait for them to leave? ').lower()
            if answer =='wait':
                print('the wolves leave because they hea a bear, the bear rips you out of the carrriage and mauls you. YOU DIED')
                if answer == 'fight':
                    print('You make quick work of the wolves and when a bear rushes you it is slain as well, nice prowess')
                    answer = input('You are hungry, will you skin and eat the bear or one if the wolves? ').lower()
                    if answer == 'bear':
                        print('One of the bears parents roars at you, and mauls you with a passion most perilous. YOU DIED')
                        if answer == 'wolf':
                            print('One of the bears parents roars at you, and mauls you with a passion most perilous. YOU DIED')
            
            
        if answer == 'ride': 
            print('You make it to your horse but the horse kicks you while trying to kick the wolves. YOU DIED')    
    
    
elif answer == 'boat':
     print('A risky choice indeed, but i surmsise you are brave')
     answer = input(
         'you set sail and the captain offers you a choice of weaponry, will you choose longsword or rapier? ').lower()
     if answer == 'longsword':
         print('the captain hands you your longsword, and you set off')
         answer = input(
             'You sail for a while and come to an island that looks beautiful beyond compare, will you dock and explore the island or keep sailing? ').lower()
         if answer == 'explore':
             print('You dock on the island and the crew decides to set up camp and find food')
             answer = input('Will you hunt for food or gather camping supplies? ').lower()
             if answer == 'hunt':
                 print('You spot what looks like a reptile like creature, you try a stab at it but it spew venom on you. YOU DIED INSTANTLY')
             if answer == 'gather':
                print('As you gather the remainer of the would you hear commotion from the rest of the crew')
                answer = input('Will you go to the crew or finish settin up camp? ').lower()
                if answer == 'finish':
                    print("You hear the captain call you, you go to him and see someone that looks i dentical to you, so you ask them their name.")
                    time.sleep(3)
                    answer = input(
                        'The stranger says no to your question so the captain shoots him in the head, you feel a jolt of pain in your own head, do you confront the captain or search the body? ').lower() 
                    if answer =='confront':
                        print('The captain shoots you as well. YOU DIED')
                        if answer == 'search':
                            print('You find a stone, pick it up, and feeling a surge of power are teleported back home. Congrats, You live to see another day!')
                    
                    
                    
                if answer == 'go':
                    print('You go to the commotion and see some one that looks exactly like you, you ask them their name.') 
                    answer = input (f'The stranger thell you that there name was, {name} so you instantly become frightened, will you interogate the stranger or stay silent? ').lower()
                    if answer == 'interogate':
                        print('You realize who has been talking to you is your own self, at this realization the stone that the stranger was holding glows red and creates a explosion so vast it destroys the whole planet, YOU DIED TWICE')
                        if answer == 'silent':
                           print('they realize who has been talking to them is your own self, at this realization the stone they were holding glows red and creates a explosion so vast it destroys the whole planet, YOU DIED TWICE')  
         
                            
             if answer == 'sail':
                 print(' The crew docks anyway and leaves makes you walk the plank for not being brave enough. YOU DIED')
         
         
     if answer == 'rapier':
         print('The captain hands you your rapier, and you set off')
         answer = input(
             'As you are sailing you and the crew see a ship comin close, will you send them a warning or will you greet them with a trade offer? ').lower() 
         if answer == 'warn':
             print('They dont heed your warning and instead cannonfire overwhelms your crew. YOU DIED')
         if answer == 'trade':
            print(' They board your shi but instead of wanting to trade they slaughter you and the crew. YOU DIED')     
              
     
        
    
    
else:
    print(' Your journey has ended before it began, what a pity.')