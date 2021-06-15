import random


class RockPaperScissors:
    def __init__(self, a, b):
        self.p = a
        self.c = b

    def play(self):
        if (self.p == 'r' and self.c == 's') or (self.p == 's' and self.c == 'p') or (self.p == 'p' and self.c == 'r'):
            print(self.c)
            return "You have won"
        elif self.p == self.c:
            print(self.c)
            return "It's a tie"
        else:
            print(self.c)
            return "You have lost"


choice = input("Want to play the game (y/n):")
if choice == 'y':
    pass
elif choice == 'n':
    exit()
else:
    raise NameError

while choice != 'n':
    print("0. Exit")
    print("1. Single Round")
    print("2. Best of Three")
    print("3. Endless Play")
    entry = int(input("Enter your option:"))
    y = random.choice(['r', 'p', 's'])

    if entry == 0:
        exit()
    elif entry == 1:
        x = input("What's your choice? 'r' for rock , 'p' for paper , 's' for scissors\n")
        obj = RockPaperScissors(x, y)
        print(obj.play())
    elif entry == 2:
        for i in range(0, 3):
            x = input("What's your choice? 'r' for rock , 'p' for paper , 's' for scissors\n")
            obj = RockPaperScissors(x, y)
            print(obj.play())
    elif entry == 3:
        while True:
            x = input("What's your choice? 'r' for rock , 'p' for paper , 's' for scissors\n")
            obj = RockPaperScissors(x, y)
            print(obj.play())
    else:
        print("Invalid choice!!")

print()
