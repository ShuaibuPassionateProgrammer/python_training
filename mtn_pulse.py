import os
import main_menu

ussd = input("Please dial a USSD code: ")

def clr():
    os.system("cls" if os.name == "nt" else "clear")

if ussd == "*406#":
    clr()
    main_menu.main_menu()
    choice = input("")

    if choice == "1":
        clr()
        print("Dear Customer, you will lose all your Pulse Points if you migrate out of the plan. do you wish to proceed?")
        print("1. Proceed")
        print("2. Cancel")
        print("\n0.Back")
        choice1 = input("")

        if choice1 == "1":
            clr()
            print("Dear Customer, you are welcome to mtn pulse. You can now enjoy calls @11KB per seconds, also you can use Night Bundle feature starting from (11:00PM - 06:00AM). Thank you")

else:
    clr()
    print("Invalid USSD code")


    