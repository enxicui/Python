'''
pseudocode

Prompt the user for integers n and k
initialize n1 = 1; k1 = 1; n2 = 1;

for every integer between 1 and n1
    n1 equals n1 * i
for every integer between 1 and k1
    n1 equals n1 * i
for every integer between 1 and n1
    n1 equals n1 * i
solutions = (n1/(k1*n2))
print(solutions)

'''

k=int(input('input combinations of',))
n=int(input('possibilities',))

n1 = 1
k1 = 1
n2 = 1
for i in range(1, n+1):
    n1 = n1 * i
for i in range(1, k+1):
    k1 = k1 * i;
for i in range(1, n - k +1):
    n2 = n2 * i
solutions = (n1/(k1*n2))
print('The total number of different combinations of toppings is', solutions)
