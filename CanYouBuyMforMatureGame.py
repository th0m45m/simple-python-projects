import datetime

#ask for customer's year of birth
yob = int(input('What year were you born (yyyy)?'))
#ask for customer's month of birth
mob = int(input('What month were you born (mm)?'))
#ask for customer's day of birth
dob = int(input('What day were you born (dd)?'))
#define today
today = datetime.date.today()
#define birthday
birthday = datetime.date(yob,mob,dob)
#formula for difference between today and birthday in days
diff = today - birthday
#converts days to years (excluding leap years)
age = diff.days/365

#If you're 17 and older, you can purchase the game.
if age >= 17:
    print('Good to go!')
#If you're younger than 17, you need parent approval to purchase the game.
else:
    print('Parent approval required.')