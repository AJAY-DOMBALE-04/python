'''
snake water gun game
snake=1
water=-1
gun=0
'''
import random

computer=random.choice([1,-1,0])
youstr=input("enter your choice :")
youdict={"s":1,"w":-1,"g":0}
reverse_str={1:"snake",-1:"water",0:"gun"}
you=youdict[youstr]

print(f"you chose :{reverse_str[you]}\n computer chose :{reverse_str[computer]}")
     
if(computer==you):
    print("its a draw !")

else:
    if(computer==1 and you==-1):
        print("you lose !")
    elif(computer==1 and you==0):
        print("you win !")
    elif(computer==-1 and you==1):
        print("you win !")
    elif(computer==-1 and you==0):
        print("you lose!")
    elif(computer==0 and you==-1):
        print("you win !")
    elif(computer==0 and you==1):
        print("you lose !")
    else:
        print("some went wrong please try again !")             