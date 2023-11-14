sum = 8900
while True:
    print("欢迎来到煎饼银行：")
    print("查询余额，\t输入[1]")
    print("存款，\t\t输入[2]")
    print("取款，\t\t输入[3]")
    print("退出煎饼银行,\t输入[4],")
    print("隐藏之修改金额，输入[-1]")

    def que():
        print(f"您的余额还有{sum}")

    def top_up():
        global sum
        sum += float(input("请输入存款金额:\n"))
        print(f"存款成功，当前余额剩余{sum}")
    def wit():
        global sum
        sum -= float(input("请输入取款金额:\n"))
        print(f"取款成功，当前余额剩余{sum}")
    def mod():
        global sum
        sum = float(input("改成多少，直接整：" ))
        print("修改成功，太刑了")
    choice = int(input())
    if choice == 1 :
        que()
        continue
    if choice == 2:
        top_up()
        continue
    if choice == 3:
        wit()
        continue
    if choice == -1:
        mod()
        continue
    if choice == 4:
        break
    if choice != -1 and choice not in [1,2,3,4]:
        print("请输入正确的数字在[1,2,3,4]之间")
print("煎饼银行为您服务!不给五星好评噶你腰子！")
