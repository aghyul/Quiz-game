def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score += 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again: ")
            attempt += 1
    if attempt == 3:
        print("The Correct answer is ", answer)


score = 0
print("Welcome to the Animal Quiz")

# Question 1
guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "Polar bear")

# Question 2
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "Cheetah")

# Question 3
guess3 = input("Which is the largest animal? ")
check_guess(guess3, "Blue Whale")

# Question 4
guess4 = input("What are baby goats called? ")
check_guess(guess4, "Kids")

# Question 5
guess5 = input("What is the smallest mammal in the world? ")
check_guess(guess5, "Bumblebee Bat")

# Question 6
guess6 = input("What type of animal is the largest primate in the world? ")
check_guess(guess6, "Gorilla")

# Question 7
guess7 = input("What is the fastest bird in the world? ")
check_guess(guess7, "Peregrine Falcon")

# Question 8
guess8 = input("What is the scientific name for a horse? ")
check_guess(guess8, "Equus ferus caballus")

# Question 9
guess9 = input("What is a group of flamingos called? ")
check_guess(guess9, "Flamboyance")

# Question 10
guess10 = input("What is the only continent without bees? ")
check_guess(guess10, "Antarctica")

# Question 11
guess11 = input("What is the most poisonous snake in the world? ")
check_guess(guess11, "Inland Taipan")

# Question 12
guess12 = input("What is the only mammal that can fly? ")
check_guess(guess12, "Bat")

# Question 13
guess13 = input("What is the most venomous spider in the world? ")
check_guess(guess13, "Brazilian Wandering Spider")

# Question 14
guess14 = input("What is the largest species of bird? ")
check_guess(guess14, "Ostrich")

# Question 15
guess15 = input("What is the fastest sea animal? ")
check_guess(guess15, "Sailfish")

# Question 16
guess16 = input("What is a group of rhinos called? ")
check_guess(guess16, "Crash")

# Question 17
guess17 = input("What is the largest land animal? ")
check_guess(guess17, "African Elephant")

# Question 18
guess18 = input("What is the name for a baby kangaroo? ")
check_guess(guess18, "Joey")

# Question 19
guess19 = input("Which animal is capable of regenerating its limbs? ")
check_guess(guess19, "Starfish")

# Question 20
guess20 = input("What is the smallest species of monkey?")
check_guess(guess20, "wistiti")
     
print("Your Score is "+ str(score))