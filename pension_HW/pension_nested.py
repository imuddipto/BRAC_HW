gov= False
ff=False

age=int(input("Please input your age: "))
x=input("Are you a government officer? (y/n): ")
if(x=='y'):
    gov = True
y=input("Are you a freedom fighter? (y/n): ")
if(y=='y'):
    ff = True

if(gov):
    if(ff):
        if(age > 59):
            print("You are eligible for pension with 30% bonus")
        else:
            print("You will be eligible for pension with 30% bonus in the future ")
    else:
        if(age > 59):
            print("You are eligible for pension")
        else:
            print("You will be eligible for pension in the future")
else:
    print("You are not eligible for pension")
