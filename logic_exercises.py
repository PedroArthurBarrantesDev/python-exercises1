
# 1 - Ask the user to enter a number and then use an if-else structure to determine if the number is even or odd.

# The 'main' function of the first app
def first_app(number):
    # Checks to see if the variable number MOD by 2 equals to 0, if true then the number is even, otherwise it is an odd number.
    if number % 2 == 0:
        print(f'The number {number} is an even number! Nice!')
    else:
        print(f'The number {number} is an odd number! How interesting...')

# 2 - Ask the user for their age and, based on it, use an if-elif-else structure to classify the age into categories according to the following conditions:

# Child: 0 to 12 years old;
# Teen: 13 to 18 years old;
# Adult: above 18 years old.

def age_choice():
    # Asks the user for his age
    print('Please enter your age in years: ')
    # Takes the input from the user and stoers it in variable age
    age = input()
    # returns the variable casting it from string to integer
    return int(age)

def age_decide(age):
    # If the age is between 0 and 12, the person is a child, if 13 to 18, a teenager, if older than 18 (ie. 19, 22, 25...), the person is an adult.
    if age >= 0 and age <= 12:
        print('You are a child!')
    elif age >= 13 and age <= 18:
        print('You are a teen!')
    else:
        print('You are an adult!')

# The 'main' function of the second app
def second_app():
    age_decide(age_choice())

# 3 - Ask for a username and a password and use an if-else structure to check if the provided username and password match the expected values determined by you.

# The 'main' function of the third app
def third_app(login_user, pass_user):
    USERNAME = 'Pedroso'
    PASSWORD = '123'

    if login_user == USERNAME and pass_user == PASSWORD:
        return f'Welcome, {login_user}!'
    else:
        return f'Incorrect username or password!'

# 4 - Ask the user for the coordinates (x, y) of any point and use an if-elif-else structure to determine in which quadrant of the Cartesian plane the point is located according to the following conditions:

# First Quadrant: x and y values must be greater than zero;
# Second Quadrant: x value is less than zero and y value is greater than zero;
# Third Quadrant: x and y values must be less than zero;
# Fourth Quadrant: x value is greater than zero and y value is less than zero;
# Otherwise: the point is located on the axis or at the origin.

# The 'main' function of the fourth app
def fourth_app(x, y):

    if (x > 0 and y > 0 ):
        print("Your coordinates are in the first quadrant!")
    elif (x < 0 and y > 0):
        print("Your coordinates are in the second quadrant!")
    elif (x < 0 and y < 0):
        print("Your coordinates are in the third quadrant!")
    elif (x > 0 and y < 0):
        print("Your coordinates are in the fourth quadrant!")
    else:
        print(f"Your coordinates are X: {x} and Y: {y}, the origin of the plane.")

# Function created to determine which app will be selected by the user.
def choose_app():
    # While loop to check if the typed option in variable 'choice' is an valid integer and not a string
    while True:
        try:
            # displays main menu
            print('Please choose your program: \n')
            print('''𝟙 - 𝕆𝕕𝕕 𝕠𝕣 𝔼𝕧𝕖𝕟 𝕟𝕦𝕞𝕓𝕖𝕣''')
            print('''𝟚 - ℂ𝕙𝕚𝕝𝕕, 𝕥𝕖𝕖𝕟 𝕠𝕣 𝕒𝕕𝕦𝕝𝕥''')
            print('''𝟛 - ℙ𝕒𝕤𝕤𝕨𝕠𝕣𝕕 𝕘𝕦𝕖𝕤𝕤𝕖𝕣''')
            print('''𝟜 - 𝕏 𝕒𝕟𝕕 𝕐 𝕔𝕠𝕠𝕣𝕕𝕚𝕟𝕒𝕥𝕖𝕤''')
            print('\nAwaiting your input: ')
            choice = int(input())

            # Switch/Case statement added in Python 3.10 or later, known as match case
            match choice:
                case 1:
                    # First program chosen
                    print('Please enter an integer number: ')
                    number = int(input())
                    first_app(number)
                
                case 2: 
                    # Second program chosen
                    second_app()
                
                case 3:
                    # Third program chosen
                    print('Please enter your Username: ')
                    username = str(input())
                    print('Now please enter your Password: ')
                    password = str(input())
                    print(third_app(username, password))
                
                case 4:
                    # Fourth program chosen
                    print('Please input the X coordinate: ')
                    x = int(input())
                    print('Please input the Y coordinate: ')
                    y = int(input())
                    fourth_app(x, y)
                
                case _:
                    print('Invalid choice! ') 

            break
        # if the user entered a string or a different type than integer, the loop asks for a valid input using try except
        except ValueError:
            print('''𝕀𝕟𝕧𝕒𝕝𝕚𝕕 𝕤𝕖𝕝𝕖𝕔𝕥𝕚𝕠𝕟. ℙ𝕝𝕖𝕒𝕤𝕖 𝕖𝕟𝕥𝕖𝕣 𝕒 𝕟𝕦𝕞𝕓𝕖𝕣 𝕓𝕖𝕥𝕨𝕖𝕖𝕟 𝟙 𝕒𝕟𝕕 𝟜❕''')
    
# the main application
def main():
    choose_app()

if __name__ == '__main__':
    main()