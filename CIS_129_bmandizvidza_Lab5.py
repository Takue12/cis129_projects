# Brendon Mandizvidza
# Lab 5: The Bottle Return Program
# 03/03/2025

# Step 1: Declare variables
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = "y"

# Step 2: Loop to run program again
while keepGoing == "y":
    NBR_OF_DAYS = 7
    totalBottles = 0
    counter = 1
    while counter <= NBR_OF_DAYS:
        print("Enter number of bottles returned for day #", counter, ":")
        todayBottles = int(input())
        totalBottles += todayBottles
        counter += 1

    # calc_payout code
    PAYOUT_PER_BOTTLE = 0.10
    totalPayout = totalBottles * PAYOUT_PER_BOTTLE

    # print_info code
    print("The total number of bottles collected is", totalBottles)
    print("The total paid out is $", totalPayout)
    print("Do you want to enter another week’s worth of data?")
    print("(Enter y or n)")
    keepGoing = input().lower()
