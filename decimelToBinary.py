'''
This script is code stub for CodeChef problem code D2BIN1_PY
Filename:      D2BIN1_PY_solution.py
Created:       27/09/2021
Last Modified: 27/09/2021
Author:        e-Yantra Team
'''

# Function to calculate Euclidean distance between two points
def dec_to_binary(n, list):
    if n > 1:
        dec_to_binary(n // 2, list)
    # print(n % 2, end = '')
    list.append(n%2)


# Main function
if __name__ == '__main__':
    
    # take the T (test_cases) input
    test_cases = int(input())
    val=[None]*test_cases
    # Write the code here to take the n value
    for case in range(0,test_cases):
        # take the n input values
        val[case] = int(input())

        # Once you have the n value, call the dec_to_binary function to find the binary equivalent of 'n' in 8-bit format
    for case in range(0,test_cases):
        ans=[0]
        dec_to_binary(val[case], ans)
        ans.remove(0)
        while(len(ans)<8):
            ans = [0] + ans

        for i in(ans):
            print(i,end="")

        print("")