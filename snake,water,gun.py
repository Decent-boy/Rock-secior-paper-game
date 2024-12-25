from sty import fg,rs,ef
import random
import time
game=["snake","water","gun"]
random_number=random.choice(game)
def player():
    while True:
        try:
            user=input(f"{fg.da_black}{ef.b}chose one from this {game}:{rs.all} ")
            # print(random_number)
            if user.lower().strip()==random_number:
                print(f"{fg.green}{ef.i}Loding...{rs.all}")
                time.sleep(3)
                print(f"{fg.cyan}{ef.i}{ef.u}game draw{rs.all}")
            elif (user.lower().strip()=="snake" and random_number=="water")or(user.lower().strip()=="water" and random_number=="gun")or (user.lower().strip()=="gun" and random_number=="snake"):
                print(f"{fg.green}{ef.i}Loding...{rs.all}")
                time.sleep(3)
                print(f"{fg.cyan}{ef.i}{ef.u}you has won{rs.all}")
                break
            else:
                print(f"{fg.green}{ef.i}Loding...{rs.all}")
                time.sleep(3)
                print(f"{fg.cyan}{ef.i}{ef.u}sorry{rs.all}")
        except ValueError:
            print(f"{fg.green}{ef.i}Loding...{rs.all}")
            time.sleep(3)
            print(f"{fg.red}{ef.i}{ef.u}Invalid{rs.all}")
while True:
    try:

        user2=input("would you like to play y or n:")
        if user2.lower().strip()=="y":
            player()
        else:
            print("ok")
            quit()
    except ValueError:
        print("invalid")