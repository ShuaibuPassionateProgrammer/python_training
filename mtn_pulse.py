ussd = input("Please dial a USSD code: ")

if ussd == "*406#":
    print("We can now proceed")
else:
    print("Invalid USSD code")