import random
print("your turn buddy ")
def guess(x):
       random_numb=random.randint(0,x)
       gussed=0
       while gussed != random_numb :
              gussed=int(input(f"guess the number between 0 to {x} :\n"))
              if gussed!= random_numb :
                     print(f"sorry  try  again buddy {gussed} is the false one")
       print(f"ohh yeah buddy you have gussed it {gussed} is the right one ")
guess(4)
print("now it our buddy computer turn ")
def computer_guess(x):
       low=1
       high=x
       feedback=""
       while feedback != "c":
              random_numb=random.randint(low,high)
              print(random_numb)
              feedback=input("is the guessed numb correct'c' if yes 'l' if low \
        and 'h' if high  ").lower
       print ("ohhh dear buddy computer you are right ..")
computer_guess(3)