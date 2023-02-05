
import random
def main(computer_option = None):
   options_dictionary = {1:"Rock",2:"Paper",3:"Scissors"}
   if computer_option is None:
      computer_option = random.randint(1,3)
   computer_choice = options_dictionary[computer_option]
   # Implement your code HERE. Usen computer_choice to obtain computer play
   
    
# Do not remove the lines below
if __name__ == "__main__":
    main()