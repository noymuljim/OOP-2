list=[1,2,3,4,5,6]

even_count=0
odd_count=0
sum_of_even=0
sum_of_odd=0

for x in list:
    if x%2==0:
        even_count=even_count+1
        sum_of_even=sum_of_even+x
    else:
        odd_count=odd_count+1
        sum_of_odd=sum_of_odd+x

print(f"sum of even ={sum_of_even}")
print(f"sum of odd= {sum_of_odd}")
print(f"odd count= {odd_count}")
print(f"even count= {even_count}")

