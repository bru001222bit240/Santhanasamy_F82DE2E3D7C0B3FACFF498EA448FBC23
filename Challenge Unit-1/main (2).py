# determines whether a year entered by the user is a leap year or not
def IsLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 ==0:
     return True
  else:
     return False
# To get year (integer input) from the user    
year = int(input("Enter a year: "))
if IsLeapYear(year):
        print('{} is a leap year.'.format(year))
else: 
      print('{} is not a leap year.'.format(year))