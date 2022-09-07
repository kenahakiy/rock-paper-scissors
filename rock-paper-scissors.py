import random

print ("Welcome to Rock, Paper, Scissors")
print ("Your options are listed below")
print (" 1. Rock")
print (" 2. Paper")
print (" 3. Scissors")
p1 = int(input("Enter the number for your selection:"))
if p1 == 1:
    hand1 = "Rock"
elif p1 == 2:
    hand1 = "Paper"
elif p1 == 3:
    hand1 = "Scissors"

shoot = [3, 1, 2, 3, 1, 2]
p2 = random.choice(shoot)

if p2 == 1:
    hand2 = "Rock"
elif p2 == 2:
    hand2 = "Paper"
elif p2 == 3:
    hand2 = "Scissors"

if shoot[p2] == shoot[p1 + 1]:
    print('lose')
elif shoot[p2] == shoot[p1 - 1]:
    print('win')
else:
    print('tie')
print(hand1)
print(hand2)