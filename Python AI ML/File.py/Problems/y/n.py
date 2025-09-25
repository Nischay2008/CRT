while True:
    print("Are you okay with the design for ppt \n")
    z = input("Enter your name: ")
    x = input("Enter your answer in (Y,N)").lower()
    y = ['y' , 'n']
    
    if x not in y:
        raise ValueError("Invalid Entry")

    count = 0
    no_c = 0

    if x == 'y':
        print(f"{z} voted a yes. Thankyou!")
        count += 1

    elif x == 'n':
        print(f"{z} voted a No. Thankyou!")
        no_c += 1

    print(f" Count of yes is {count} and Count of no is {no_c}")