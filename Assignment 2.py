#Number 1
print("This is Number 1.\n")
Hours = input("Enter Hours: ")
Hours = int(Hours)
print(Hours,"hours\n")

Rate = input("Enter Rate: ")
Rate = float(Rate)
print(Rate,"rate\n")

Salary = Hours * Rate
print("This is the Salary: ",Salary)
print("\n")

#Number 2
print("This is Number 2.\n")
Celsius = input("Enter Celsius: ")
Celsius = int(Celsius)
print(Celsius,"degree celsius\n")
Fahrenheit = (Celsius * 9 / 5 + 32)
print("This is the Fahrenheit: ",Fahrenheit)
print("\n")

#Number 3
print("This is Number 3.\n")
Seconds = input("Enter Seconds: ")
Seconds = float(Seconds)
print("\n")
Hour = (Seconds // 3600)
Minutes = ((Seconds % 3600) // 60)
Seconds1 = (Seconds % 60)
print("therefore,the inputted Seconds is,",Hour,"hours,",Minutes,"minutes,",Seconds1,"seconds.")
print("\n")
print("Rackhel Fernando Lovies Byanto, 202312229, Assignment 2.")