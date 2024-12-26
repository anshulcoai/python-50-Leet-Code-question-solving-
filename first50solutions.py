

# 1.Check if a number is positive.
'''
a=int(input("Enter a Number :"))
print(a)
if a>0:
    print("Its a positive number")
elif a==0:
    print("Its a Zero")
     
else:
    print("This is not a positive number")
'''

# 2.Check if a number is negative.
'''
a=int(input("Enter a number :"))
print(a)
if a<0:
    print("Its a negative number")
elif a==0:
    print("Its a zero")
else:
    print("This is not a negative number")
'''

# 3. Check if a number is zero.
'''
a=int(input("Enter a number :"))
print(a)
if a==0:
    print("Number is Zero")
else:
    print("Number is not zero")
'''

# 4. Check if a number is even.
'''
a=int(input("Enter a number :"))
print(a)
if a%2==0:
    print("Number is even")
else:
    print("Number is not even")
'''

# 5. Check if a number is odd.
'''
a=int(input("Enter a number :"))
print(a)
if a%2!=0:
     print("Number is odd")
else:
     print("Number is not odd")
'''

# 6. Determine if a character is a vowel.
'''
a=(input("Enter any character:"))
print(a)
if a=='a' or a=='A' or a=='e' or a=='E' or a=='i' or a=='I' or a=='o' or a=='O' or a=='u' or a=='U':
    print("This character is vowel")
else:
    print("This is a normal character")
'''

# 7. Determine if a character is a consonant.
'''
a=(input("Enter any character :"))
print(a)
if a=='a' or a=='A' or a=='e' or a=='E' or a=='i' or a=='I' or a=='o' or a=='O' or a=='u' or a=='U':
    print("This is not consonant")
else:
    print("This is consonant")
'''

# 8. Determine if a character is uppercase.
'''
a=(input("Enter any character :"))
print(a)
if a>='A' and a<='Z':
    print("This character is uppercase")
else:
    print("This character is not an uppercase")
'''

# 9. Determine if a character is lowercase.
'''
a=(input("Enter any character :"))
print(a)
if a>='a' and a<='z':
    print("This character is lowercase")
else:
    print("This character is not lowercase")
'''

# 10. Check if a character is a digit.
'''
a=(input("Enter any character :"))
print(a)
if a>='a' and a<='z' or a>='A' and a<='Z':
    print("This is not a digit")
else:
    print("This is a digit")
'''

# 11. Find the larger of two numbers.
'''
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
print("First number is :",a)
print("Second number is :",b)
if a>b:
    print("First number is greater :",a)
else:
    print("Second number is greater :",b)
'''

# 12. Find the smaller of two numbers.
'''
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
print("First number is :",a)
print("Second number is :",b)
if a<b:
    print("First number is smaller :",a)
else:
    print("Second number is smaller :",b)
'''

# 13. Find the largest of three numbers.
'''
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
c=int(input("Enter a third number :"))
print("First number is :",a)
print("Second number is ",b)
print("Third number is :",c)
if a>b and a>c:
    print("First number is larger :",a)
elif b>a and b>c:
    print("Second number is larger :",b)
else:
    print("Third number is larger :",c)
'''

# 14. Find the smallest of three numbers.
'''
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
c=int(input("Enter a third number :"))
print("First number is :",a)
print("Second number is ",b)
print("Third number is :",c)
if a<b and a<c:
    print("First number is smallest",a)
elif b<a and b<c:
    print("Second number is smallest",b)
else:
    print("Thirs number is smallest",c)
'''

# 15. Check if a year is a leap year.
'''
a=int(input("Enter a Year :"))
print("Year :",a)
if a%4==0:
    print(a,"year is a leap year")
else:
    print("This is not a leap year")
'''

# 16. Check if a number is divisible by 5.
'''
a=int(input("Enter a number :"))
if a%5==0:
    print("Yes",a,"is divisble by 5")
else:
    print("No",a," is not divisible by 5")
'''

# 17. Check if a number is divisible by 11.
'''
a=int(input("Enter a number :"))
if a%11==0:
    print("Yes",a,"is divisible by 11")
else:
    print("No",a,"is not divisble by 11")
'''

# 18.Determine if a number is between 10 and 100.
'''
a=int(input("Enter a number :"))
if a>10 and a<100:
    print("Number is between 10 and 100")
else:
    print("Number is not between 10 and 100")
'''

# 19.Determine if a number is outside the range 10 to 100.
'''
a=int(input("Enter a number :"))
if a>10 and a<100:
    print("Number is between 10 and 100")
else:
    print("Number is Out of Range")
'''

# 20.Check if the sum of two numbers is positive.
'''
a=int(input("Enter a First Number :"))
b=int(input("Enter a Second Number :"))
c=a+b
print(c)
if c>0:
    print("Sum is positive")
else:
    print("Number is not positive")
'''

# 21.Check if the sum of two numbers is negative.
'''
a=int(input("Enter a First Number :"))
b=int(input("Enter a Second Number :"))
c=a+b
print(c)
if c<0:
    print("Sum is negative")
else:
    print("Number is not negative")
'''

# 22.Check if the sum of two numbers is zero.
'''
a=int(input("Enter a First Number :"))
b=int(input("Enter a Second Number :"))
c=a+b
print(c)
if c==0:
    print("Sum is Zero")
else:
    print("Sum is not Zero")
'''

# 23.Determine if a person is eligible to vote (age >= 18).
'''
a=int(input("Enter Age of Person :"))
if a>=18:
    print("This person is eligible to vote")
else:
    print("This is person is not eligible to vote")
'''
    
# 24.Determine if a person is a teenager (age between 13 and 19).
'''
a=int(input("Enter Age of person :"))
if a>=13 and a<=19:
    print("Person is teenager")
else:
    print("Person is not teenager")
'''

# 25.Determine if a person is a senior citizen (age >= 60).
'''
a=int(input("Enter Age of a Person :"))
if a>=60:
    print("Person is a senior citizen")
else:
    print("Person is not a senior citizen")
'''

# 26.Check if the product of two numbers is positive.

'''
a=int(input("Enter a First Number :"))
b=int(input("Enter a Second Number :"))
c=a*b
print(c)
if c>0:
    print("Product is positive")
else:
    print("Product is not positive")
'''

# 27.Check if the product of two numbers is negative.
'''
a=int(input("Enter a First Number :"))
b=int(input("Enter a Second Number :"))
c=a*b
print(c)
if c<0:
    print("Product is negative")
else:
    print("Product is not negative")
'''

# 28.Check if the product of two numbers is zero.
'''
a=int(input("Enter a First Number :"))
b=int(input("Enter a Second Number :"))
c=a*b
print(c)
if c==0:
    print("Product is zero")
else:
    print("Product is not zero")
'''

# 29. Check if a character is an alphabet letter.
'''
a=(input("Enter any key on keyboard :"))
print(a)
if a>='a' and a<='z' or a>='A' and a<='Z':
    print("Its an alphabet")
else:
    print("Its not an alphabet")
'''

# 30.Check if a character is not an alphabet letter.
'''
a=(input("Enter any key on keyboard :"))
print(a)
if a<'a' or a>'z' and a<'A' or a>'z':
    print("It is not an alphabet")
else:
    print("It is an alphabet")
'''

# 31.Determine if a number is a single-digit number.
'''
a=int(input("Enter a number :"))
print(a)
if a>0 and a<10:
    print("It is a single-digit number")
else:
    print("It is not single-digit number")
'''

# 32.Determine if a number is a double-digit number.
'''
a=int(input("Enter a number"))
print(a)
if a>=10 and a<100:
    print("It is a double-digit number")
else:
    print("It is not a double-digit number")
'''
 
# 33.Determine if a number is a triple-digit number.
'''
a=int(input("Enter a number :"))
print(a)
if a>=100 and a<1000:
    print("It is a triple-digit number")
else:
    print("It is not a triple-digit number")
'''

# 34.Determine if a number is greater than or equal to 100.
'''
a=int(input("Enter a number :"))
print(a)
if a>100:
    print("Number is greater than 100")
elif a==100:
    print("Number is equals to 100")
else:
    print("Number is not greater than 100")
'''

# 35.Determine if a number is less than or equal to 100.
'''
a=int(input("Enter a number :"))
print(a)
if a<100:
    print("Yes number is less than 100")
elif a==100:
    print("Number is equal to 100")
else:
    print("This number is not less than or equal to 100")
'''

# 36.Determine if a year is a century year.--------doubt

# 37.Find the absolute value of a number.
'''
a=int(input("Enter any number :"))

if a>0:
        print(a," is the absolute value" )
else:
        print(a*-1,"is the absolute value")
'''

# 38.Check if a character is an uppercase vowel.
'''
a=(input("Enter any character :"))
print(a)
if a=='A' or a=='E' or a=='I' or a=='O' or a=='U':
    print("Character is an uppercase vowel")
else:
    print("Character is not an uppercase vowel")
'''

# 39.Check if a character is a lowercase vowel.
'''
a=(input("Enter any character :"))
print(a)
if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
    print("Character is lowecase vowel")
else:
    print("Character is not lowercase vowel")
'''

# 40.Check if a number is a perfect square.
'''
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
c=a*b
print(c)
if a==b:
    print("Yes this is a perfect square")
else:
    print("No this is not a perfect square")
'''

# 41.Determine if a number is within 10 of 100.
'''
a=int(input("Enter a number :"))
print(a)
if a>=90 and a<=110:
    print("Number is within 10 of 100")
else:
    print("Number is not within 10 of 100")
'''

# 42.Determine if a number is within 20 of 200.
'''
a=int(input("Enter a number :"))
print(a)
if a>=180 and a<=220:
    print("Number is within 20 of 200")
else:
    print("Number is not within 20 of 200")
'''

# 43.Check if a number is divisible by 2 and 3.
'''
a=int(input("Enter a number :"))
print(a)
if a%2==0 and a%3==0:
    print("Yes number is divisible by 2 and 3")
else:
    print("No Number is not divisible by 2 and 3")
'''

# 44.Check if a number is divisible by 2 or 3.
'''
a=int(input("Enter a number :"))
print(a)
if a%2==0 or a%3==0:
    print("number is divisible by 2 or 3")
else:
    print("Number is not divisible by 2 or 3")
'''


# 45.Check if a number is not divisible by 2 or 3.
'''
a=int(input("Enter a number :"))
print(a)
if a%2!=0 or a%3!=0:
    print("Number is not divisible by 2 or 3")
else:
    print("Number is divisible by 2 or 3")
'''

#46.Determine the middle value of three numbers.
'''
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
c=int(input("Enter a third number :"))

if a<b and b>c:
    print(c,"is the middle value of a number")
elif a<b and b<c:
    print(b,"is the middle value of a number")
else:
    print(a,"is the middle value of a number")
'''

# 47.Find the second largest of three numbers.
'''
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
c=int(input("Enter a third number :"))

if a>b and a<c or a>c and a<b:
    print(a,"is the second largest of three numbers")
elif b>a and b<c or b>c and b<a:
    print(b,"is the second largest of three numbers")
else:
    print(c,"is the second largest of three numbers")
'''

# 48.Find the second smallest of three numbers.
'''
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
c=int(input("Enter a third number :"))

if a<b and a>c or a<c and a>b:
    print(a,"is the second smallest number")
elif b<a and b>c or b<c and b>a:
    print(b,"is the second smallest number")
else:
    print(c,"is the second smallest number")
'''

# 49.Check if a number is prime. --------doubt

# 50.Check if a number is composite (not prime and >1).
'''
a=int(input("Enter a number "))
print(a)
if a%2==0 or a%3==0 or a%5==0 or a%7==0 or a%11==0 or a>1:
        print("Number is a composite number")
else:
    print("Number is not a composite number")
'''        
    


















    


    





















    




















































    





































 
    
    


























