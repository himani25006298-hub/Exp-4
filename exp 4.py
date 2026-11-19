CODE
number = [10,20,30,40,50]
print("original list:",number)

print("length:",len(number))

number.append(60)
print("After append:",number)

number.insert(2,25)
print("After insert:",number)

number.remove(25)
print("after remove:",number)

number.pop()
print("after pop:",number)

print("count of 20:",
      number.count(20))

print("index of 30:",
      number.index(30))

number.sort()
print("after sort:",number)

number.reverse()
print("after reverse:",number)

new_list = number.copy()
print("copied list:",new_list)

number.extend([70,80])
print("after extend:",number)

print("maximum:",max(number))

print("minimum:",min(number))

print("sum:",sum(number))

number.clear()
print("after clear:",number)
      


OUTPUT:

original list: [10, 20, 30, 40, 50]
length: 5
After append: [10, 20, 30, 40, 50, 60]
After insert: [10, 20, 25, 30, 40, 50, 60]
after remove: [10, 20, 30, 40, 50, 60]
after pop: [10, 20, 30, 40, 50]
count of 20: 1
index of 30: 2
after sort: [10, 20, 30, 40, 50]
after reverse: [50, 40, 30, 20, 10]
copied list: [50, 40, 30, 20, 10]
after extend: [50, 40, 30, 20, 10, 70, 80]
maximum: 80
minimum: 10
sum: 300
after clear: []
