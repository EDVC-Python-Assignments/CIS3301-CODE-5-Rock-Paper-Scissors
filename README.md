## CIS3301-CODE-5-Rock-Paper-Scissors

In this CODE assignment, you are going to program a simple Rock-Paper-Scissors game. The game will execute once and the user has the chance of winning, losing or tying with the computer. Below is the logic the game should have:

* Rock beats Scissors
* Paper beats Rock
* Scissors beats Paper
* It is a tie when the user and the computer choose the same option. For example Paper vs. Paper

## User prompts

* The user is greeted
  + **"\nWelcome to the Game of Rock, Paper Scissors"**
* The user is asked for their option
  + **"Choose from the options below\n"**
  + **"1. Rock"**
  + **"2. Paper"**
  + **"3. Scissors"**
  + **"\nEnter your option:"**
* The following messages should be displayed to the user depending on the draw of the computer
  + Tie: **"It is a tie"**
  + The user wins: **"You won! user_option beats computer_option"** (replace user_option and computer_option)
  + The user loses: **"You lose! computer_option beats user_option"** (replace user_option and computer_option)

## Tip

* Use the dictionary `options_dictionary` to compare your output
* The logic of the game can be implemented using if, elif(s), and else
* One side comparison when implementing the logic is effective. In other words implement the logic focusing in one player.
