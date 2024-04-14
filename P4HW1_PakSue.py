# Sue Pak
# 4/14/2024
# P4HW1
# Assignment created to collect each score and loop them

num_scores = int(input("How many scores do you want to enter? "))
scores = []

for i in range(1, num_scores + 1):
    score = float(input(f"Enter score #{i}: "))
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i} again: "))
    scores.append(score)

lowest_score = min(scores)

modified_scores = scores.copy()
modified_scores.remove(lowest_score)

average_score = sum(modified_scores) / len(modified_scores)

if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print()
print('\n-------------Results-----------')
print(f"Lowest Score  : {lowest_score:.1f}")
print(f"Modified List : {modified_scores:}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {letter_grade}")
print('---------------------------------')
