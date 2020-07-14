def Pythangorean_Checker():
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))
    d = max(a, b, c) # Where the maximum number becomes the hypothenus which is the longest side
    
    if a**2 + b**2 == d**2: # formular a^2 + b^2 = c2
        print("It is a pythangorean triple")

    elif a**2 + b**2 != d**2:
        print ("It is not a pythangorean triple")
        next = input("Do you want to continue: Yes or No: ")

        if next == "Yes":
            Pythangorean_Checker()

        else:
            print("Okay. Thanks for trying. Bye for now.")

Pythangorean_Checker()


