'''
This script is code stub for CodeChef problem code APLAM1_PY
Filename:      APLAM1_PY_solution.py
Created:       27/09/2021
Last Modified: 27/09/2021
Author:        e-Yantra Team
'''

# Import reduce module
from functools import reduce


# Function to generate the A.P. series
def generate_AP(a1, d, n):

    AP_series = []
    current_value = a1

    for i in range(0, n):
        AP_series.append(current_value)
        current_value = current_value + d
    # Complete this function to return A.P. series


    return AP_series


# Main function
if __name__ == '__main__':
    
    # take the T (test_cases) input
    test = int(input())
    ans=[]
    ans_square=[]
    # Write the code here to take the a1, d and n values
    for i in range(test):
        a1,d,n = map(int,input().split())

        # Once you have all 3 values, call the generate_AP function to find A.P. series and print it
        AP_series = generate_AP(a1, d, n)
        ans.append(AP_series)
        ans_square=list(map(lambda x: x ** 2, AP_series))
        ans.append(ans_square)
        ans.append([reduce(lambda a, b: a+b, ans_square)])


    for x in ans:
        print(*x, sep=' ')
    print(" ")
#Hello using this for git hub

#New branch working 
        