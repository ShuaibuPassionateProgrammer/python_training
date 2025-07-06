import os
import sys

ussd = input("Please dial a USSD code: ")

def clr():
    os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    print("1. Join Pulse")
    print("2. 1.2GB+1hr(YT/IG/TT) @N750")
    print("3. Nightlife Bundles")
    print("4. IG/Tiktok/Youtube Bundles")
    print("5. Goodybag")
    print("6. 750MB @N450")
    print("7. Pulse Points")
    print("8. Campus Zone")

def join_pulse():
    print("Dear Customer, you will lose all your Pulse Points if you migrate out of the plan. do you wish to proceed?")
    print("1. Proceed")
    print("2. Cancel")
    print("\n0.Back")

while True:
    if ussd == "*406#":
        clr()
        main_menu()
        choice = input("")

        if choice == "1":
            clr()
            join_pulse()
            choice1 = input("")

            if choice1 == "1":
                clr()
                print("Dear Customer, you are welcome to mtn pulse. You can now enjoy calls @11KB per seconds, also you can use Night Bundle feature starting from (11:00PM - 06:00AM). Thank you")
            elif choice1 == "2":
                clr()
                sys.exit(0)
            elif choice1 == "0":
                clr()
                main_menu()

    else:
        clr()
        print("Invalid USSD code")


    