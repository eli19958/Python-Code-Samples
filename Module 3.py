#Elizabeth Montero
#2/4/2022

#Problem 1
print("Hello World")


#Problem 2
name=input('Enter your name:')
print('Hello, ' + name)

#Problem 3
#Put your name
name= input( 'Enter your name: ' )
#Enter either Alice or bob to print name
if name == "bob" or name == "alice":
    print(' Hello, ' + name)

#Problem 4
pi = (3.14)
r = input("Please type radius of your circle:")
r = float(r)
#Caculate to get answer
area= pi * r **2
print("Area of the circle is", area)


#Problem 5
#Get miles from the driver
miles_driven = input("Enter miles driven:")
miles_driven = float(miles_driven)
#Get gallons from driver 
gallons_used = input("Enter gallons used:")
gallons_used = float(gallons_used)
mpg = miles_driven/ gallons_used
#Calculate to get answer
print(" Miles per gallon:", mpg)



#Problem 6
fer = float(input('Enter Fahrenheit Temperature: '))
#Calculation to convert from Fahrenheit to Celsius
cel = (fer - 32) * 5/9
print('Celsius Temperature: {0}'.format(cel))


#Problem 7

vacationStart=int(input('What day does your vacation start? (Enter 0 for Sunday, 1 for monday, etc.) '))
vacationLength=int(input('How many days will your vacation be? '))
#Calculates and divides to figure out the return day
returnDay=(vacationLength+vacationStart)%7

print(returnDay)
