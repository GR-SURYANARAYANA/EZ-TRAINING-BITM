"""
3) Chocolate jar
You are given an integer array of size N, representing jars of chocolates. Three students A, B, and C respectively, will pick chocolates one by one from each chocolate jar, till the jar is empty, and then repeat the same with the rest of the jars. Your task is to fine and return an integer value representing the total number of chocolates that student A will have, after all the chocolates have been picked from all the jars.
Note: Once a jar is done A will start taking the chocolates from the new jar.

Input Format :
input1: An integer array representing the quantity of chocolates in each jar. input2: An integer value N representing the number of jars.

Output Format:
Return an integer value representing the total number of chocolates that student A will have, after all the chocolates are picked.

Example:

Input:
10 20 30

Output:
21

Explanation:
Jar 1: 10 chocolates -> A-4, B-3,C-3
Jar 2: 20 chocolates -> A-7, B-7, C-6 Jar 3: 30 chocolates -> A-10, B-10,C-10 so A gets a total of 4+7+10=21 chocolates.
"""

jar = map(int,input().split(" "))
a_s_count = 0 
for i in jar:
  a_s_count = a_s_count + i//3 + (0 if i%3==0 else 1)
print(a_s_count)