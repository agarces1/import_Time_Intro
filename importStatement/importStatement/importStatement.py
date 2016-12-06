#imports datetime library
import datetime
#store the value in a variable called currentDate.
currentDate = datetime.date.today();
#print(currentDate);
#print(currentDate.year);
#print(currentDate.month);
#print(currentDate.day);
#strftime allows you to specify the date format
#print(currentDate.strftime('%d %b,%Y'));
userInput = input ("Please enter your birthday! mm/dd/yyyy ");
birthdate = datetime.datetime.strptime(userInput, "%m/%d/%Y").date();
#why did I list datetime twice?
#because we are calling the strptime function
#which is part of the datetime class
#which is in the datetime module
print(birthdate);
#print days since your birthday
days = currentDate - birthdate
print(days);
