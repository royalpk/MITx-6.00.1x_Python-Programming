'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
 For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

'''

s = 'azcbobobegghakl'
past_count=0
long_sub=s[0]
temp=s[0]
for i in range(len(s) -1):
    if s[i+1]>=s[i]:
        temp=temp+s[i+1]
        if len(temp)>past_count:
            past_count=len(temp)
            long_sub=temp
    else:
        temp=s[i+1]
print(long_sub)