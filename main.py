from game_data import data
from art import logo, vs
from replit import clear
import random

def check_answer(guess, player_A, player_B):
  if player_A['follower_count'] > player_B['follower_count']:
    return guess == 'a'
  else:
    return guess == 'b'

score = 0
while True:
  # print logo
  print(logo)
  
  # choose 2 random player
  player_A = random.choice(data)
  player_B = random.choice(data)

  if player_A == player_B:
    clear()
    continue
    
  # print 1 against 2
  print(f"Compare A: {player_A['name']}, {player_A['description']} from {player_A['country']}")
  print(vs)
  print(f"Against B: {player_B['name']}, {player_B['description']} from {player_B['country']}")
  
  # input answer
  user_answer = input("Who has more followers? A or B? ").lower()
  print(check_answer(user_answer, player_A, player_B))

  clear()
  
  if check_answer(user_answer, player_A, player_B):
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    break


    # answer = ""
  # if player_A['follower_count'] > player_B['follower_count']:
  #   answer = "a"
  # else:
  #     answer = "b"
  
  # clear()

  # if user_answer == answer:
  #   score += 1
  #   print(f"You're right! Current score: {score}")
  # else:
  #   print(f"Sorry, that's wrong. Final score: {score}")
  #   break
