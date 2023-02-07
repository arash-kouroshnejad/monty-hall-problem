import random
# Now let’s do that 100000 times.
# Make 10000 trials.
n_tries = 10000000
# Lists to store results from stay and switch strategy
stay_results = []
switch_results1 = []
switch_results2 = []
for i in range(n_tries):
    # Same code as above, for one trial
    doors = ['car', 'goat', 'goat', 'goat']
    random.shuffle(doors)
    my_door_index = random.choice([0, 1, 2, 3])
    stay_result = doors.pop(my_door_index)
    doors.remove('goat')
    switch_result1 = doors[0]
    switch_result2 = doors[1]
    # Put results into result lists
    stay_results.append(stay_result)
    switch_results1.append(switch_result1)
    switch_results2.append(switch_result2)


print(stay_results.count('car') / n_tries)

print(switch_results1.count('car') / n_tries)

print(switch_results2.count('car') / n_tries)