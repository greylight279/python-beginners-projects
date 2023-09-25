import random
work=input("enter the work you love!\n :")
hero=input("name the favourite hero \n:")
animal=input("name any  animal\n :")

madlib1=(f"Hey it feels nice to be {work} .I hope i will be {hero} doing {work}\
 because I am in love with {animal} that i want to do  marriage with {animal}")
madlib2=(f"{work} is my thing. i can be {animal} doing my {work} but sure one \
 day i will die as a {hero} alltoug i am an {animal}")
madlib3=(f"i am an {animal} who love to {work} and i will be {hero} of {animal} one\
 day for sure")

madlib=random.randint(1,3)
if madlib ==1 :
       print(madlib1)
elif madlib==2 :
       print(madlib2)
else:
       print(madlib3)
sorry=("man,sum")