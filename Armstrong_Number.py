def check_armstrong():
    numbers = int(input("Please enter your numbers: "))
    length = len(str(numbers))
#     print(length)
# check_armstrong()
    total_sum = 0
    if len(str(numbers))== 1:
        print("All single digits are Armstrong numbers")
    elif numbers < 0:
        print("Enter a positive number")
    else:
        for i in str(numbers):
            total_sum += int(i)**length
        if total_sum == numbers:
            print("This is an Armstrong numbers")
        else:
            print("This is NOT an Armstrong number")
check_armstrong()