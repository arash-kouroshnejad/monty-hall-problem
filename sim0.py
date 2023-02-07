import random
# Now let’s do that 100000 times.
# Make 10000 trials.
n_tries = 100
# Lists to store results from stay and switch strategy
stay_results = []
switch_results = []
for i in range(n_tries):
    # Same code as above, for one trial
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)
    my_door_index = random.choice([0, 1, 2])
    stay_result = doors.pop(my_door_index)
    doors.remove('goat')
    switch_result = doors[0]
    # Put results into result lists
    stay_results.append(stay_result)
    switch_results.append(switch_result)

stay_results.count('car') / n_tries

switch_results.count('car') / n_tries