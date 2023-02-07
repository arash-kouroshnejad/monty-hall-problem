import random
import collections
# Now let’s do that 100000 times.
# Make 10000 trials.
n_tries = 1000000
# Lists to store results from stay and switch strategy
print(">>> enter the number of doors")
door_count = int(input())
switch_results = []
stay_results = []
for i in range(n_tries):
    # Same code as above, for one trial
    doors = ['car', 'goat']
    for i in range(door_count - 2):
        switch_results.append(collections.deque())
        doors.append('goat')
    random.shuffle(doors)
    my_door_index = random.choice(range(door_count))
    stay_result = doors.pop(my_door_index)
    doors.remove('goat')
    # Put results into result lists
    stay_results.append(stay_result)
    for i in range(door_count - 2):
        switch_results[i].append(doors[i])
    
    doors.clear()


print(" holding : " + str(stay_results.count('car') / n_tries))

for i in range(door_count - 2):
    print(" switching " + str(i) + " : " + str(switch_results[i].count('car') / n_tries))