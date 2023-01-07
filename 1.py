lower = int(input("Lower range limit:"))
upper = int(input("Higher range limit:"))
num = int(input("Number to be divided by:"))

for i in range(lower,upper+1):
    if(i%num==0):
        print(i)
