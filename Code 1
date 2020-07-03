'''
Write a program to find the character which appears the most in a string, and then replace all occurrences of this character with the second most frequently appearing character in this string.
Details:
The program should first find the character which appears the most in the string, and then replace the character throughout the string with the next most frequently appearing character.
Inputs:
Input the string for working on.
Outputs:
The output should contain 2 lines:-
First line will be the character which appears the most
Second will be the new string with its most frequent character replaced by the next most frequent character in the string.
Sample:

Inputs
bbabbbaaabccd

Outputs:
b
aaaaaaaaaaccd

Explanation:- The most occuring character was b, and second most was a, so all b were replaced by a.

'''

#Here is the code

x = input() #we took the input
s=[]
y=[]
for k in x:
    s.append(k)
    y.append(k)
s.sort()
#print(s)
ss = []
ss.append(s[0])
for jj in s:
    #print(jj)
    if(jj not in ss):
        ss.append(jj)
#print(ss)
counts  = []
for i in ss:
	counts.append(s.count(i))
 
countss = sorted(counts)
#print(countss)
no1 = counts.index(countss[-1])
max1 = ss[no1] #we got the maximum occuring char
no2= counts.index(countss[-2])
#print(max1)
max2 = ss[no2] #and here the second most


for n, ii in enumerate(y):
	if(ii == max1):
            y[n] = max2


for w in y:
	print(w,end='')
