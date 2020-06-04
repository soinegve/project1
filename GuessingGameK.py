import random

target = random.randint(1, 100)

dif = 100
runs = 0
current_warm_distance = 10
guess_list = []
while dif != 0:

    # each time in the loop we ask input from user once
    guess = int(input('Enter A number between 1 and 100: '))
    
    if guess <= 0 or guess > 100:
        print("Out of bounds")
        continue
        
    guess_list.append(guess)
    distance_from_target = abs(guess - target)
    
    # we print cold or warm only first time , next time we say -er
    er_or_nothing = "" if len(guess_list)==1 else"er"
    
    if distance_from_target >= current_warm_distance > 0:
        print(f'Warm{er_or_nothing}!')

    elif current_warm_distance > distance_from_target:
        print(f'Cold{er_or_nothing}!')

    current_warm_distance = distance_from_target

print(f'You guessed {target} in {len(guess_list)} tries')
