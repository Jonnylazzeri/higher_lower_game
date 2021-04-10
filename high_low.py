import random
from game_data import data

rand_1 = random.choice(data)
rand_2 = random.choice(data)
if rand_1 == rand_2:
  rand_1 = random.choice(data)
  rand_2 = random.choice(data)

game_on = True
score = 0

while game_on:

  rand_1_name = rand_1['name']
  rand_1_followers = int(rand_1['follower_count'])
  rand_1_desc = rand_1['description']
  rand_1_country = rand_1['country']

  rand_2_name = rand_2['name']
  rand_2_followers = int(rand_2['follower_count'])
  rand_2_desc = rand_2['description']
  rand_2_country = rand_2['country']

  print(f'Compare A: {rand_1_name}, a {rand_1_desc}, from {rand_1_country}')
  print(f'Against B: {rand_2_name}, a {rand_2_desc}, from {rand_2_country}')

  guess = input('Who has more followers? A or B? ').upper()

  if guess == 'A' and rand_1_followers > rand_2_followers:
    rand_1 = rand_2
    rand_2 = random.choice(data)
    score += 1
    print(f'Correct! Current score: {score}')
  elif guess == 'B' and rand_2_followers > rand_1_followers:
    score += 1
    rand_1 = random.choice(data)
    rand_2 = random.choice(data)
    print(f'Correct! Current score: {score}')
  else:
    print(f"Sorry, that's wrong. Final Score: {score}")
    break