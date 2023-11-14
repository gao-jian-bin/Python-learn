import random
sum = 10000
for i in range(1,21):
    suc  = random.randint(1,10)
    if suc < 5:
        print(f"员工{i}的绩效是{suc},不发工资，下一位")
        continue
    else:
        sum -= 1000
        print(f"向员工{i}发工资1000元，账户余额{sum}元")
    if sum == 0:
        print("工资发完了")
        break


