# Lesson 10: Simple Recursive Function

This code explains a simple recursive function that increments a number until it reaches or exceeds 9.

#### Code Explanation:
1. **Function Definition**:
   ```python
   def add_one(num):
   ```
   - Defines a function 

add_one

 that takes a single argument 

num

.

2. **Base Case**:
   ```python
   if (num >= 9):
       return num + 1
   ```
   - If 

num

 is greater than or equal to 9, the function returns 

num + 1

.

3. **Recursive Case**:
   ```python
   total = num + 1
   print(total)
   return add_one(total)
   ```
   - Otherwise, it increments 

num

 by 1, prints the new value, and calls itself with the new value.

4. **Function Call**:
   ```python
   mynewtotal = add_one(0)
   print(mynewtotal)
   ```
   - Calls the 

add_one

 function with 0 and prints the final result.

### 

game_rps.py



This code explains a Rock, Paper, Scissors game where the user plays against the computer.

#### Code Explanation:
1. **Imports and Enum Definition**:
   ```python
   import sys
   import random
   from enum import Enum
   ```
   - Imports necessary modules and defines an enumeration for Rock, Paper, Scissors.

2. **Function Definition**:
   ```python
   def play_rps():
   ```
   - Defines the main function 

play_rps

 for the game.

3. **Game Loop**:
   ```python
   playagain = True
   while playagain:
   ```
   - Initializes a loop that continues as long as 

playagain

 is `True`.

4. **User Interface**:
   ```python
   title = " Game: Rock, Paper, Scissors (RPS) ".upper()
   print(title.center(50, "" + ("=") + ""))
   ```
   - Prints the game title and instructions.

5. **User Input**:
   ```python
   playerchoice = input("Enter your choice: ")
   player = int(playerchoice)
   ```
   - Prompts the user to enter their choice and converts it to an integer.

6. **Computer Choice**:
   ```python
   computerchoice = random.choice("123")
   computer = int(computerchoice)
   ```
   - Randomly selects a choice for the computer.

7. **Determine Winner**:
   ```python
   if player == 1 and computer == 3:
       print("Rock crushes scissors. 🎉 You win!")
   ```
   - Compares the player's choice with the computer's choice to determine the winner.

8. **Play Again Prompt**:
   ```python
   playagain = input("Enter 'y' to continue or 'n' to exit: ")
   if playagain.lower() == "y":
       return play_rps()
   else:
       sys.exit("Bye! Bye! Bye! 👋👋👋 \n\n")
   ```
   - Asks the user if they want to play again and either restarts the game or exits.

### 

example.py



This code explains a loop that prompts the user to enter values and continues based on user input.

#### Code Explanation:
1. **Initialization**:
   ```python
   import sys
   value = "y"
   count = 0
   ```
   - Imports the 

sys

 module and initializes 

value

 to "y" and 

count

 to 0.

2. **Main Loop**:
   ```python
   while value.lower() == "y":
   ```
   - Continues the loop as long as 

value

 is "y".

3. **Increment and Print Count**:
   ```python
   count += 1
   print(count)
   if count == 5:
       print("You have reached the maximum number of tries.")
       break
   ```
   - Increments and prints the count. If the count reaches 5, it breaks the loop.

4. **User Input**:
   ```python
   value = input("Enter a value: ")
   if value.lower() == "n":
       break
   if not value.isdigit():
       print("Invalid input. Please enter a number.")
       continue
   if int(value) > 5:
       print("You entered a number greater than 5. Please try again.")
       continue
   ```
   - Prompts the user to enter a value and checks if it's a valid number. If the value is greater than 5, it asks the user to try again.

5. **Continue Prompt**:
   ```python
   print("You entered: " + value)
   print("Would you like to continue?")
   value = input("Enter 'y' to continue or 'n' to exit: ")
   ```
   - Prints the entered value and asks if the user wants to continue.

6. **Exit**:
   ```python
   sys.exit("Bye! Bye! Bye! 👋👋👋 \n\n")
   ```
   - Exits the program with a goodbye message.