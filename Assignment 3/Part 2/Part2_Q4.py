# Q4: Get first and second best scores from the list

Scores_list = [40, 89, 90, 89, 23, 90, 50]

first_best = max(Scores_list)

while first_best in Scores_list:
    Scores_list.remove(first_best)

second_best = max(Scores_list)

print("First Best Score:", first_best)
print("Second Best Score:", second_best)
