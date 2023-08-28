#Problem 4: Luhn's algorithm
import functools
def add(n1,n2):
    return int(n1)+int(n2)
def double(n):
    return int(n)*2
def list_to_string(list):
    strings = ''
    for i in list:
        strings =strings+str(i)
    return strings

card_number=list(input('Please enter your card number: '))
#getting a list of every other digit starting from second to last
mult_digits=[]
for i in range(len(card_number)-2,-1,-2):
    mult_digits.append(card_number[i])
#the digits after they double:
mult_digits = list(map(double,mult_digits))
#convert the array to a string
doubled = list_to_string(mult_digits)
#convert the string to an array f char
mult_digits = list(doubled)
#add those digits
sum_of_doubled = functools.reduce(add,mult_digits)

#put the every other digit starting from LAST in a list
not_doubled=[]
for i in range(len(card_number)-1,-1,-2):
    not_doubled.append(card_number[i])
#add those digits
sum_of_notdoubled=functools.reduce(add,not_doubled)

#get the total sum
total_sum=sum_of_doubled+sum_of_notdoubled
if total_sum%10 !=0 :
    print('Invalid')
else:
    if card_number[0]+''+card_number[1] == '34' or card_number[0]+''+card_number[1] == '37':
        print('American Express')
    elif card_number[0] =='4':
        print('Visa')
    else:
        print('MasterCard')