import random
from statistics import mean
from statistics import mode
from statistics import median

list_of_scores = []
number_of_attempts = 0

def select_difficulty(chosen_difficulty):
  global solution
  if chosen_difficulty == "easy":
    solution = random.randrange(1, 11)
  elif chosen_difficulty == "normal":
    solution = random.randrange(1, 101)
  elif chosen_difficulty == "hard":
    solution = random.randrange(1, 1001)
  else:
    solution = random.randrange(1, 1000001)
  return solution


def welcome_msg(times_played):
  if times_played == 1:
    print("Welcome to the 2022 GOTY") 
  elif times_played < 3:
    print("Are you sure? Don't you have anything better to do? Ok then. At least this game has less bugs than Cyberpunk...")
  elif times_played <= 4:
    print("ALL YOUR BASE ARE BELONG TO US!")
  elif times_played > 4:
    print("Here we go again...")

        
def solution_range_indicator_msg():
  if solution >= 1 and solution <=10:
    print("Coward... The solution will be between 1 and 10")
  elif solution >= 1 and solution <=100:
    print("Ok, the solution will be between 1 and 100. Let's go")
  elif solution >= 1 and solution <=1000:
    print("This is going to take some time. The solution is between 1 and 1000")
  else:
    print("Wrong answer, now you will never guess the number. Good luck!")

        
def manage_user_input():
  global number_of_attempts
  print("Ok, time to guess")
  number_of_attempts = 0
  fails = 0
  
  while True:
    move = input("Enter a number: \n > ")
    try:
      answer = int(move)
      if difficulty == "easy":
        if answer > 10 or answer < 1:
          print("Naaah! Out of range.")
          continue
      elif difficulty == "normal":
        if answer > 100 or answer < 1:
          print("Naaah! Out of range.")
          continue
      elif difficulty == "hard":
        if answer > 1000 or answer < 1:
          print("Naaah! Out of range.")
          continue
      else:
        if answer > 1000000 or answer < 1:
          print("Naaah! Out of range.")
          continue
        
      if answer == solution:
        number_of_attempts += 1
        if number_of_attempts == 1:
          print(f"WINNER, WINNER, CHICKEN DINNER! You made it in {number_of_attempts} time.\nData police is studying your case, you will see your stats once you finish your game session.")
          score(number_of_attempts)
        else:
          print(f"WINNER, WINNER, CHICKEN DINNER! You made it in {number_of_attempts} times.\nData police is studying your case, you will see your stats once you finish your game session.")
          score(number_of_attempts)
        break
      elif answer < solution:
        print("It's higher")
        number_of_attempts += 1
        continue
      elif answer > solution:
        print("It's lower")
        number_of_attempts += 1
        continue
    except Exception:
      if move == "f":
        print("Don't go! Play my game! The cat food is expensive and my cat is hungry! I need the money!")
        if number_of_attempts != 0:
          final_stats(list_of_scores)
        exit()
      elif fails == 0:
        print("We miss roman numbers class, try a numeric one")
        fails += 1
      elif fails == 1:
        print("Are you nervous? It's numbers only \n...Meh! I don't care, press any key... any key but 'f'")
        fails += 1
      elif fails == 2:
        print("These TKL keyboard users... The numeric pad is tier S!")
        fails += 1
      else:
        print("Daddy chill! This is a tilt free space!")
        if number_of_attempts != 0:
          final_stats(list_of_scores)
        exit()
      continue    
  return number_of_attempts


def score(new_score_to_add):
  global list_of_scores
  list_of_scores.append(new_score_to_add)
  list_of_scores.sort()
  return list_of_scores


def final_stats(stats_to_analyze):
  if len(stats_to_analyze) != 0:
    stat_average = mean(stats_to_analyze)
    stat_most_times = mode(stats_to_analyze)
    stat_middle_game = median(stats_to_analyze)
    stat_best_game = min(stats_to_analyze)
    print(f"Are you really leaving? Ok, let's summarize: \n -Your average score: {stat_average} \n -Most repeated score: {stat_most_times} \n -And your best score: {stat_best_game}")
    print("I'm telling you this before you leave just in case you want to keep playing this wonderful game and be a better version of yourself. My Paypal is...")
  else:
    print("You didn't even try it. Rude")


def game_loop(games_played):
  global difficulty
  welcome_msg(games_played)
  print("Select difficulty: 'easy', 'normal' or 'hard'")
  difficulty = input("> ")
  select_difficulty(difficulty.lower())
  solution_range_indicator_msg()
  manage_user_input()
    
    
def start_game(): 
  print("Game Started!")
  games_played_counter = 0
  restart = ""
  
  if games_played_counter == 0:
    games_played_counter += 1
    game_loop(games_played_counter)
        
  while True:
    restart = input("Do you want to play again? (y/n) \n > ")
    if restart.lower() != "y" and restart.lower() != "n":
      restart = input("What? I didn't understand. Do you want to play again? (y/n) \n > ")        
            
    if restart.lower() == "y":
      games_played_counter += 1
      game_loop(games_played_counter)
    elif restart.lower() == "n":
      final_stats(list_of_scores)
      print("Bye! T_T")
      exit()

            
start_game()
