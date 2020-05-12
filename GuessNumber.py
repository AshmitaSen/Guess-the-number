import random
def main():
    a=random.randint(0,10)
    n=3
    print("You have 3 choices")
    for i in range(3,0,-1):
        x=int(input("Enter number:"))
        if a==x:
            print("Congrats! You Win")
            break
        elif i-1==0:
            print("Sorry! No more chances left! The number is ",a)
            
        else:
            print("You have ",i-1," chances left")
if __name__=="__main__":
    main()
