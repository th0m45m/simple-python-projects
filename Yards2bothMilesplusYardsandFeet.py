#User prompt to enter number of yards
yards = int(input("Enter a positive number of yards:"))
#miles calculated
miles = int(yards // 1760)
#remainder in yards if mile total is not whole number
yards_remaining = int(yards % 1760)
#number of feet
feet = int(yards * 3)
#shows what user entered
print("You entered", yards, "yards, which is:")
#shows distance in miles with the remainder of yards (if applicable)
print(miles, "miles and", yards_remaining, "yards")
#or
print("or")
#shows distance in feet
print(feet, "feet")