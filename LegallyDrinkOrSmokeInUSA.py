import datetime

yob = int(input('What year were you born (yyyy)?')) #ask for customer's year of birth
mob = int(input('What month were you born (mm)?')) #ask for customer's month of birth
dob = int(input('What day were you born (dd)?')) #ask for customer's day of birth
today = datetime.date.today() #define today
birthday = datetime.date(yob,mob,dob) #define birthday
diff = today - birthday #formula for difference between today and birthday in days
age = diff.days/365 #converts days to years (excluding leap years)

#If you're younger than 18, you cannot legally smoke or drink.
if age < 18:
    print('You are not allowed to drink or smoke in accordance with state laws.')
    
#If you're at least 18 but younger than 21, you cannot have an alcoholic beverage.
else:
    if age >= 18 and age < 21:
        print('You may smoke on premises, but by law, you cannot have an alcoholic beverage.')
    else:
        print('You may enjoy a smoke and an alcoholic beverage during your visit.')