import random 
import time 
from sty import Style,fg,RgbFg,ef,rs
fg.light_coral=Style(RgbFg(240,128,128))
fg.deep_sky_blue=Style(RgbFg(0,191,255))
fg.chocolate=Style(RgbFg(210,105,30))

try:
    Name=input(f"{fg.black}{ef.b}Enter Your name:{rs.all} ")
    age=int(input(f"{fg.black}{ef.b}Enter Your age:{rs.all} "))
    if age>=10 and age<=80:
            
        print(f"{fg.light_coral}{ef.i}{Name}{rs.all}")
        print(f"{fg.light_coral}{ef.i}{age}{rs.all}")
        print(f"{fg.chocolate}{ef.i}WELLCOME TO ROCK SECIOR AND PAPER GAME{rs.all}")
        print(f"{fg.green}{ef.i}Loding....{rs.all}")
        time.sleep(2)
        print(f"{fg.chocolate}{ef.b}__________________{rs.all}")
    else:
        print(f"{fg.green}{ef.i}Loding....{rs.all}")
        time.sleep(2)
        print(f"{fg.deep_sky_blue}{ef.i}your age is not inserted!{rs.all}")
except ValueError:
    print(f"{fg.green}{ef.i}Loding....{rs.all}")
    time.sleep(2)
    print(f"{fg.red}{ef.b}Error{rs.all}")
user_score=0
computer_score=0
options=["rock","secior","paper"]
while True:
    try:
        user_input=input(f"{fg.light_coral}{ef.i}Type one (Rock/Secior/Paper) and Q for (quit){rs.all}{fg.black}{ef.b}\nType Here: {rs.all}")
        if user_input.lower().strip()=="q":
            print(f"{fg.deep_sky_blue}{ef.i}Done!{rs.all}")
            print(f"{fg.green}{ef.i}Loding....{rs.all}")
            time.sleep(2)
            quit()
        elif user_input.lower().strip() not in options:
            continue
        random_number=random.randint(0,2)
        computer_pick=options[random_number]
        print(computer_pick)
        if (user_input=="rock" and computer_pick=="secior") or \
        (user_input=="secior" and computer_pick=="paper") or\
        (user_input=="paper" and computer_pick=="rock"):
            print(f"{fg.green}{ef.i}Loding....{rs.all}")
            time.sleep(2)
            print(f"{fg.light_coral}{ef.i}You has won\n congrutlation{rs.all}")
            print(f"{fg.chocolate}{ef.b}.............{rs.all}")
            user_score+=1
        elif user_input==computer_pick:
            print(f"{fg.green}{ef.i}Loding....{rs.all}")
            time.sleep(2)
            print(f"{fg.deep_sky_blue}{ef.i}The game has been draw{rs.all}")
        else:
            print(f"{fg.green}{ef.i}Loding....{rs.all}")
            time.sleep(2)
            print(f"{fg.light_coral}{ef.i}You has been losed{rs.all}")
            computer_score+=1
        print(f"{fg.light_coral}{ef.i}your total score is {user_score} {rs.all}")
        print(f"{fg.light_coral}{ef.i}Computer score is {computer_score} {rs.all}")
    except ValueError:
        print(f"{fg.red}{fg.b}Error{rs.all}")