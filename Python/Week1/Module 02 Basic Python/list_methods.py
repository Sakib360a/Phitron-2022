number = [20,10,30]
number.append(2)
number.append(2)
number.append(2)
print(number)
number.pop()
number.pop(0) #pop also takes index
value = number.pop() #pop also gives deleted value
print(number)
number.insert(2,40)
print(number)

number.remove(30)
print(number)
number.append(23)
number.append(23)
number.append(23)
number.append(23)
if 8 in number:
    number.remove(8)
if 23 in number:
    number.remove(23)
print(number)

search_index = number.index(23) #gives the first occurance also
print(search_index)
if -5 in number:
    search_index = number.index(-5)


number.sort()
print(number)

number.reverse()
print(number)