#Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other.
 
def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;
print(test_distinct([1,5,7,9]))


#Write a Python program that accept a positive number and subtract from this number the sum of its digits and so on. Continues this operation until the number is positive.

n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)

#Write a Python program to find the digits which are absent in a given mobile number

def absent_digits(n):
  all_nums = set([0,1,2,3,4,5,6,7,8,9])
  n = set([int(i) for i in n])
  n = n.symmetric_difference(all_nums)
  n = sorted(n)
  return n
print(absent_digits([7,7,2,2,0,4,6,7,6,2]))



#Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

import itertools
s='AEIOU'
t=list(itertools.permutations(s,len(s)))
for i in range(0,len(t)):
    print (''.join(t[i]))

#Write a Python program to find common divisors between two numbers in a given pair.

a = 12
b = 24
n = 0
  
for i in range(1, min(a, b)+1): 
    if a%i==b%i==0: 
        n+=1
      
print(n) 


