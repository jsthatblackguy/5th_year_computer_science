name = input("whats the name of the football club you support:")
no1 = input("how many wins have you guys had:")
no1 = float(no1)
no2 = input("how many draws have u guys had:")
no2 = float(no2)
no3 = input("how many loses have youy guys had:")
no3 = float(no3)
total1 = no1 * 3
total2 = no2 * 1
total3 = no3 * 0
total4 = total1 + total2 + total3
print(name,"has",total4,"this season")