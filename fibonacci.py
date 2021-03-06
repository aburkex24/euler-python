#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#Euler #2

# algo to get fibonacci numbers under 1 mil
#   then only get the even numbers

count = 0
first = 0
next = 0
sum = 0

while count <= 4_000_000:
    if count is 0:
        first = count
        next = count + 1

    count = first + next
    if count % 2 is 0:
        sum += count
    
    first = next
    next = count

print(sum)