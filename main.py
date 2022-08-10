import art 
from game_data import data
import random
from replit import clear

#fetches random accounts from the data set
def get_random_account():
  return random.choice(data)

# checks if the answer is correct
def check_answer(guess, followers_a, followers_b):
  if followers_a > followers_b:
    return guess == "a"
  else:
    return guess == "b"

def format(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return (f"{name}, a {description} from {country}")


def the_game():
  score = 0
  continue_game = True 
  account_a = get_random_account()
  account_b = get_random_account()
  print(art.logo)
  while continue_game: 
    account_a == account_b
    account_b = get_random_account()
    
    while account_a == account_b:
      account_b = get_random_account() 

    print(f"Compare A: {format(account_a)}")
    print(art.vs)
    print(f"Compare B: {format(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B'? ").lower()

    followers_a_count = account_a["follower_count"]
    followers_b_count = account_b["follower_count"]
    is_correct = check_answer(guess, followers_a_count,followers_b_count)
    
    clear()
    print (art.logo)
    if is_correct: 
      score += 1
      print(f"Correct! Your current score is {score}")
    else:
      print (f"Sorry, thats wrong. Your final score is: {score}")
      continue_game = False
    

the_game() 
    
    



