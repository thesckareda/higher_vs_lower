import art
import random
from game_data import data
print(art.logo)


def number():
    ab = list(range(1,51))
    random.shuffle(ab)

    while ab:
        num = ab.pop() # picks a random number, never repeating
        return num

def format_date(account):
    acc_name = account["name"]
    acc_des = account["description"]
    acc_city = account["country"]
    return f"{acc_name}, a {acc_des}, from {acc_city}"

acc_b = random.choice(data)

score = 0


game_over = True

while game_over:
    acc_a = acc_b
    acc_b = random.choice(data)

    if acc_a == acc_b:
        acc_b = random.choice(data)


    fc1 = acc_a['follower_count']
    print(f"Compare A: {format_date(acc_a)}")
    print(art.vs)
    fc2 = acc_b['follower_count']

    print(f"Against B: {format_date(acc_b)}")
    type = input("Who has more followers? Type 'A' or 'B': ")
    if fc1 > fc2 and type == "A" or fc1 < fc2 and type == "B":
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        game_over = False


