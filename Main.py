# Carmelo Espino
# This is the start of a small video game where you manage a city
# Extra resources used: https://www.asciiart.eu/text-to-ascii-art

import secrets

# Intro
def intro(): # Defines the intro function
    print("                 ", "Welcome", "to", sep=' ') # Uses sep= to seperate statements with a space
    print(""" __  __                               _ _     
|  \/  | ___  _ __   ___  _ __   ___ | (_)___ 
| |\/| |/ _ \\| '_ \\ / _ \\| '_ \\ / _ \\| | / __|
| |  | | (_) | | | | (_) | |_) | (_) | | \\__ \\
|_|  |_|\\___/|_| |_|\\___/| .__/ \\___/|_|_|___/
                         |_|                   """)
    print("                 City Manager!\n")
    print("The goal of this game is to manage your city without running out of your vital resources.", end='\n') # Uses end= to end with line break
    print(". " * 3) # Uses * string operator to print '. ' 3 times
    cityName = input("Enter your city name: ") # Prompts user to input city name
    print("\nHello Mayor of " + cityName + "!") # + operator concatenates inputted city name with !
    return cityName

# Difficulty Selection
def chooseDifficulty():
    while True: # While loop to ensure user inputs a valid response
        difficulty = input("Pick your difficulty: Easy, Medium, or Hard. (Type E, M, or H): ")
        if difficulty == "E": # Checks if inputted difficulty == E
            print("You have selected Easy difficulty.")
            return 375, 350, 325
        elif difficulty == "M":
            print("You have selected Medium difficulty.")
            return 300, 275, 250
        elif difficulty == "H":
            print("You have selected Hard difficulty.")
            return 200, 175, 150
        else:
            print("Invalid difficulty, please try again.")

# Winter Event
def winterEvent(money, food, population): # Function accepts money food and population parameters
    print("Event: Winter has arrived and many of the crops have died.")
    print("The people ask you to fund trade for more food to prepare.")
    while True:
        try:
            cost = int(input("How much money will you allocate for trade? $"))
            if cost < 0 or cost > money: # Checks if inputted cost is less than zero OR more than user has
                print("Invalid amount, try again.")
            elif cost >= 125: # Else checks if inputted cost is greater than or equal to 125
                money -= cost
                food -= (25 + (0 ** 2)) # Decrements by 25 plus 0 squared which equals 25
                population -= 10
                print("You acted sufficiently and withstood minimal damage!")
                break
            elif cost >= 85:
                money -= cost
                food -= (50 + (0 * 2)) # Decrements by 50 plus 0x2 which equals 50
                population -= 25
                print("Your donation worked moderately and the damages were okay.")
                break
            else: # Else / if all other if statements are false
                money -= cost
                food -= (75 + (0 / 2)) # Decrements by 75 plus 0/2 which equals 75
                population -= 30
                print("You underestimated the effects of winter and suffered serious setbacks.")
                break
        except ValueError:
            print("Invalid input. Please try again.")
    return money, food, population

# Mining Event
def miningEvent(money, food, population):
    print("Event: The city needs raw materials. You will send men to mine steel at the local cave.")
    print("The more men you send, the higher the risk of casualties but also opportunity for more money.")
    while True:
        try:
            cost = int(input("How many men will you send to mine? "))
            if cost < 0 or cost > population:
                print("Invalid amount, try again.")
            elif cost >= 75:
                population -= cost
                money += (250 + (16 % 4)) # Increments by 250 plus the remainer of 16/4 which equals 250
                print("During the large mining expedition, the entrance collapsed and all " + str(cost) + " men were trapped and died.")
                break
            elif cost >= 60:
                population -= 50
                money += (150 + (0 // 2)) # Increments by 150 plus 0/2 rounded down which equals 150
                print("You sent a sizable mining crew. 50 men died in a mining accident.")
                break
            elif cost >= 45:
                population -= 20
                money += (100 - 0) # Increments by 100 minus 0 which equals 100
                print("You sent an optimal mining crew. Only 20 men died.")
                break
            else:
                population -= 10
                money += 50
                print("You played it safe and only 10 men died during the trip.")
                break
        except ValueError:
            print("Invalid input. Please try again.")
    return money, food, population

# Famine Event
def famineEvent(money, food, population):
    print("Event: Your neighboring ally city has hit a famine and needs your support.")
    print("You can give them food to earn money, but it will cost population.")
    while True:
        try:
            cost = int(input("How much food will you donate to your ally? "))
            if cost < 0 or cost > food:
                print("Invalid amount, try again.")
            elif cost >= 125:
                food -= cost
                population -= 60
                money += 100
                print("You supported your friends generously.")
                break
            elif cost >= 60:
                food -= cost
                population -= 40
                money += 50
                print("You helped your neighbor stay afloat.")
                break
            elif cost >= 30:
                food -= cost
                population -= 20
                money += 25
                print("You gave your neighbor some help; they may survive the crisis.")
                break
            else:
                food -= (cost + 100)
                population -= 125
                money -= 200
                print("Your offer insulted your ally and they ambushed you! You were forced to surrender resources.")
                break
        except ValueError:
            print("Invalid input. Please try again.")
    return money, food, population

# Bandit Event
def banditEvent(money, food, population):
    print("Event: Local bandits have raided one of our local trading centers.")
    print("We must fund to recover our losses and not face major setbacks.")
    while True:
        try:
            cost = int(input("How much money will you allocate for recovery? $"))
            if cost < 0 or cost > money:
                print("Invalid amount, try again.")
            elif cost >= 125:
                money -= cost
                food += 25
                population -= 10
                print("You responded generously and reaped the rewards!")
                break
            elif cost >= 85:
                money -= cost
                food -= 40
                population -= 15
                print("You sent enough money and the damages were okay.")
                break
            else:
                money -= cost
                food -= 70
                population -= 25
                print("Your funds were minimal and we lost many resources.")
                break
        except ValueError:
            print("Invalid input. Please try again.")
    return money, food, population

# Picking random event
def randomEvent(money, food, population):
    eventNum = secrets.randbelow(4)
    if eventNum == 0:
        return winterEvent(money, food, population)
    elif eventNum == 1:
        return miningEvent(money, food, population)
    elif eventNum == 2:
        return famineEvent(money, food, population)
    elif eventNum == 3:
        return banditEvent(money, food, population)
    elif eventNum != 4: # Checks if eventNum does not equal 4
        return

# End of Game
def endOfGame(money, food, population):
    print(". . .\nEnd of Term: ")
    print("Ending funds: $" + format(money, '.2f'))
    print("Ending food:", food)
    print("Ending population:", population)
    if money > 0 and food > 0 and population > 0: # Checks if money AND food AND pop are over 0
        print(". . .\nYou win! Your city survived your term as Mayor.")
    else:
        print(". . .\nYou lose. Your city ran out of at least one key resource during your term.")

# Main function
def main():
    cityName = intro()
    money, food, population = chooseDifficulty()
    length = int(input("How many days would you like to play? (Recommended: 5) "))
    
    for day in range(1, length + 1): # For loop using variable day in range of 1 and inputted length + 1
        print("\n. . .\nDay", day)
        print("Current funds: $" + format(money, '.2f'))
        print("Current food: " + str(food))
        print("Current population: " + str(population))
        input("\nEnter to continue. . . ")
        money, food, population = randomEvent(money, food, population)

    endOfGame(money, food, population)

# Call for Main function
if __name__ == '__main__':
    main()
