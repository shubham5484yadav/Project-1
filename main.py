import random
computer = random.choice([-1,0,1])

you_str = input("Enter your choice ")
dict_number = {"s":1, "w":-1, "g":0}
reverse_dict ={1: "Snake", -1: "Water", 0: "Gun"}
you = dict_number[you_str]
print(f"You choose {reverse_dict[you]}\ncomputer choose {reverse_dict[computer]}")

if(computer==you):
    print("its draw")
else:
    if(computer == -1 and you == 1):
        print("you win! ")
    elif(computer == -1 and you ==0):
        print("you loose!")
    elif(computer == 1 and you==0):
        print("you win")
    elif(computer ==1 and you==-1):
        print("You loose!")
    elif(computer ==0 and you ==1):
        print("you loose!")
    elif(computer ==0 and you ==-1):
        print("You Win!")
    else:
        print("Something went wrong")
