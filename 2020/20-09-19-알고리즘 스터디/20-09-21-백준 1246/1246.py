N, M = map(int, input().split())
customers = []
for m in range(M):
    customers.append(int(input()))
customers.sort(reverse=True)
total = 0
price = 0
for index, customer in enumerate(customers):
    if index+1 > N:
        break
    result = customer * (index+1)
    if result > total:
        total = result
        price = customer
print(price, total)