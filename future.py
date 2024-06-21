from datetime import datetime as dt, timedelta as td

# def future():
#     print("Welcome to the Future.\n")
#     choice = int(input("how may years do you want to view from now: "))
#     today = dt.now()
#     next = today + td(days = choice * 365)
#     print("\nwhat can you see:", (next))
# future()


from datetime import datetime as dt, timedelta as td

def Look_Into_The_Future():
    
    print("\nWelcome to the Future. \nA great One Awaits you.")
    
    while True:
        
        print("\nWhat is your prefrence: ")
        print("1. Day")
        print("2. Week")
        print("3. Month")
        print("4. Year")
        print("5. Exit")
        
        current_date = dt.now()
        print(f"Current Date: {current_date.strftime('%a %d %B, %Y')}")
        
        Choice = input("Enter 1/2/3/4: ")
            
        if Choice == "1":
            day_to_add = int(input("\n Enter the number of days to add: "))
            future_date = current_date + td(days= day_to_add)
            print(f"Future Date: {future_date.strftime('%a %d %B, %Y')} \n\nFuture Message: Your Hopes are fruitful.")
        elif Choice == "2":
            Week_to_add = int(input("\n Enter the number of days to add: "))
            future_date = current_date + td(days= Week_to_add * 7)
            print(f"Future Date: {future_date.strftime('%a %d %B, %Y')} \n\nFuture Message: Your Hopes are fruitful")
        elif Choice == "3":
            Month_to_add = int(input("\n Enter the number of months to add: "))
            future_date = current_date + td(days= Month_to_add * 30)
            print(f"Future Date: {future_date.strftime('%d, %B, %Y')} \n\nFuture Message: Your Hopes are fruitful")
        elif Choice == "4":
            Year_to_add = int(input("\n Enter the number of years to add: "))
            future_date = current_date + td(days= Year_to_add * 365)
            print(f"Future Date: {future_date.strftime('%d %B, %Y')} \n\nFuture Message: Things are materilizing")
        elif Choice == "5":
            print("See you in the Future You've dreamt of. \nBye for now >>>>")
            break
        else:
            print("\nWrong Input, Try again.")
            Look_Into_The_Future
    
Look_Into_The_Future()