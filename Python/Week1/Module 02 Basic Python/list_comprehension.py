list = [10,11,15,17,18,25,27,90, 46,45,29,44]
odd_but_divisible_by_5=[]
# for num in list:
#     if num%2!=0 and num%5==0:
#         odd_but_divisible_by_5.append(num)
# print(odd_but_divisible_by_5)

odd_but_divisible_by_5 = [num for num in list if num%2!=0 and num%5==0]
print(odd_but_divisible_by_5)

players=['sakib','musfiq','mashrafi','razzak','liton']
ages = [40,35,38,36,34]
for player in players:
    #print(player)
    for age in ages:
        print('Player:',player,age)