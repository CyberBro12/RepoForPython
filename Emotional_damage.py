import time

def troll():
    print("What is your name?")
    name1 = input("You: ")
    print("Do you want to play the game?")
    a = input("You: ")

    if a.lower() == "yes":
        print(f"Hey, {name1} do you know the name of game?")
        b = input(f"{name1}: ")
        if b.lower() == "yes":
            print(f"How do you know the name of game\n we haven't even named it")
            print(f"{name1}, you bloody liar")
            print("now try entering no when i ask you know the game?")
            troll()
        elif b.lower() == "no":
            print("Why are you playing the game if you don't eve know the name of the game.")
            time.sleep(2)
            print("Don't worry we haven't even named the game yet :>")
            print("ok let's start the game")
            guess = f'fuck you like a porn star {name1}'.split()
            for i in range(0, 1):
                for j in guess:
                    print(f"\r{j}", end='', flush=True)
                    time.sleep(0.5)
            h = 'fuck'
            print(", ok that's nasty don't dare to type fuck ok? ;D")
            b = input(f"{name1}: ")
            if b.lower() == h:
                print(f"{name1} you wanna go nasty?\nk fine with me!\n Now the darkest truths of your life.\n")
                time.sleep(1)
                print("The father you know is not your, i am your father >:)\ni slept with your mommy\n"
                      "month before\n"
                      "you were born\n")
                time.sleep(1)
                print("And i sleep with her daily! Oh! sorry\n")
                time.sleep(0.5)
                print("Your mother is calling me again\n")
                print("Bye\n")
                time.sleep(2)
                print(f"My son {name1}\n")
            elif a.lower() == "no":
                print("idc you gott play this >:(")
                troll()
            else:
                print("Nvm, Bye")
        else:
            print("why you are playing a game\nwhere you don't even know how to type yes or now dumbo")


if __name__ == '__main__':
    troll()
