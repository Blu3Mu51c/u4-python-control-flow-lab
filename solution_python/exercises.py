
# Example 0
def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()


# Example 1
def check_letter():
    letter = input("Enter an alphabet: ").lower()
    print(f"The user entered {letter}")

    if letter in ["a", "e", "i", "o", "u"]:
        print(f"The letter {letter} is a vowel")
    elif letter.isalpha():
        print(f"The letter {letter} is a consonant")
    else:
        print("Not an alphabet")

check_letter()

# Exercise 2
def check_voting_eligibility():
    user_age = input("Enter your age: ")
    print(f"Your age is {user_age}")
    age=int(user_age)
    if age <= 0:
        print(f"Invalid Parameter")
    elif age >= 18:
        print(f"You are {age} and are old enough to vote")
    else:
        print(f"You are not old enough to vote")

check_voting_eligibility()

# Exercise 3: Calculate Dog Years

def calculate_dog_years():
    user_dog = input("Enter dog age: ")
    print(f"Your dog's age is {user_dog}")

    dage=int(user_dog)
    if dage <=0:
        print(f"Invalid input try again")
    elif dage < 3:
        dog_age = dage * 10
        print(f"Dog age is {dog_age}")
    else:
        dog_age = 20 + (dage - 2) * 7 #remove the first 2 years because we already have 20 and then mult by 7
        print(f"Dog age is {dog_age}")
        
calculate_dog_years()

# Exercise 4: Weather Advice

def weather_advice():
    temp = input("Is it cold? Yes or No? ").lower()
    rain = input("Is it raining? Yes or No? ").lower()

    if temp not in ["yes", "no"] or rain not in ["yes", "no"]: #Check if input is yes or no anything else is invalid
        print("Invalid input, try again")
        return

    t = temp == "yes"
    r = rain == "yes"

    if t and r:
        print("Wear a waterproof coat")
    elif t and not r:
        print("Wear a warm coat")
    elif r and not t:
        print("Carry an umbrella")
    else:
        print("Wear light clothing")

weather_advice()


# Exercise 5: What's the Season?

def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").lower()
    day = int(input("Enter the day of the month: "))

    if (month == "dec" and day >= 21) or month in ["jan", "feb"] or (month == "mar" and day <= 19):
        print("Winter")
    elif (month == "mar" and day >= 20) or month in ["apr", "may"] or (month == "jun" and day <= 20):
        print("Spring")
    elif (month == "jun" and day >= 21) or month in ["jul", "aug"] or (month == "sep" and day <= 21):
        print("Summer")
    elif (month == "sep" and day >= 22) or month in ["oct", "nov"] or (month == "dec" and day <= 20):
        print("Fall")
    else:
        print("Invalid")


determine_season()

# Exercise 6: Number Guessing Game

def guess_number():
    target = 42
    attempts = 5

    for attempt in range(1, attempts + 1):
        guess = input(f"Attempt {attempt}: Enter your guess: ")
        
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        g = int(guess)

        if g == target:
            print("Congratulations, you guessed correctly!")
            return 
        else:
            if g < target:
                print("Guess is too low.")
            elif g > target:
                print("Guess is too high.")

            if attempt == attempts-1:
                print("Last chance!")

    print("Sorry, you failed to guess the number in five attempts.")
guess_number()
