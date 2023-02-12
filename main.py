# PART 1
# 1. Create a variable for every player that scored
player_0 = "Ruud Gullit"
player_1 = "Marco van Basten"

# 2. Create a variable for each minute of the match that a goal was scored in
goal_0 = 32
goal_1 = 54

# 3. Using the +-operator, create a string that reports on who scored when
scorers = player_0 + " " + str(goal_0) + ", " + player_1 + " " + str(goal_1)
print(scorers)

# 4.  Use f-strings or the +-operator to create a single string with information about who scored when in the format:
# <scorer_name> scored in the <when_they_scored>nd minute
# <scorer_name> scored in the <when_they_scored>th minute
# The result should be stored in a variable report.
report = f"{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute" 
print(report)

# PART 2
# 1. Choose a player that played in the soccer match and store his name as a string in the variable player.
player = player_0

# 2. first_name: use slicing and the find-method to isolate and store the player's first name.
# start_first_name = player.find('Ruud')
first_name = player[:player.find(' ')]
first_name = player_0[0:4]
print(first_name)

# 3. last_name_len: use find, slicing and len to isolate and store the length of their last name
first_name = player[:player.find(' ')]
length_name = len(first_name)
last_name = player[player.find(' ')+1:]
last_name_len = len(last_name)
print(last_name_len)

# 4. name_short: isolate and store the player's name in this format:
name_short = f"{first_name[0]}. {last_name}"
print(name_short)

#5. chant name times the length of first name no end-space
length_first_name = len(first_name)
first_name_format = f"{first_name}!"
chant = first_name_format * len(first_name)
print(chant)

# 6. check for spaces in chant
chant = (((first_name + "! ") [:7]) * len(first_name)) [:34]
print(chant)

good_chant = chant[5] != " "
print(good_chant)

# Tips check
winc = "Ruud Gullit scored in the 32nd minute Marco van Basten scored in the 54th minute"
me = "Ruud Gullit scored in the 32nd minute Marco van Basten scored in the 54th minute"
ok = print(winc == me)


