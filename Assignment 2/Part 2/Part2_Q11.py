
#11. Squares of numbers from 1 to 10

sum_even = 0
sum_odd = 0

for i in range(1, 51):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)
