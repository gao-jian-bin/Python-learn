# if float(input("身高超过120需要购票输入你的身高\n")) > 120.0:
#     if int(input("很遗憾，但是会员等级超过3级可以半价，输入您的会员等级：\n")) > 3:
#         print("恭喜您，可以半价购票")
#     else:
#         print("对不起，您需要原价购票")
# else:
#     print("恭喜您，可以免费购票")
# age = int(input("快点输入年龄!:\n"))
#
# if age >= 18 and age <=30 :
#     year = int(input("快点输入入职年数!:\n"))
#     lev = int(input("快点输入会员等级!:\n"))
#     if year >= 2 or lev >=3 :
#         print("可以领取礼物")
#     else:
#         print("不好意思，您不能领取")
# else:
#     print("不好意思，年龄过大，您不能领取")

import random
tar = random.randint(1,10)
print(tar)
num = int(input("输入你想猜测的数字\n"))
if num == tar:
    print("恭喜您，一次就猜对了")
elif num < tar:
    num = int(input("您猜测的小了,请再猜测一次\n"))
    if num == tar:
        print("恭喜您，用两次猜对了")
    elif num < tar:
        num = int(input("您猜测的又小了，请再猜测一次\n"))
        if num == tar:
            print("恭喜您，最后一次猜对了")
        else :
            print("对不起，您机会用完了，没有猜对")
    else:
        num = int(input("您猜测的大了,请再猜测一次\n"))
        if num == tar:
            print("恭喜您，用两次猜对了")
        elif num < tar:
            num = int(input("您猜测的又小了，请再猜测一次\n"))
            if num == tar:
                print("恭喜您，最后一次猜对了")
            else:
                print("对不起，您机会用完了，没有猜对")
else:
    num = int(input("您猜测的大了,请再猜测一次\n"))
    if num == tar:
        print("恭喜您，用两次猜对了")
    elif num < tar:
        num = int(input("您猜测的小了，请再猜测一次\n"))
        if num == tar:
            print("恭喜您，最后一次猜对了")
        else:
            print("对不起，您机会用完了，没有猜对")
    else:
        num = int(input("您猜测的大了,请再猜测一次\n"))
        if num == tar:
            print("恭喜您，用两次猜对了")
        elif num < tar:
            num = int(input("您猜测的小了，请再猜测一次\n"))
            if num == tar:
                print("恭喜您，最后一次猜对了")
            else:
                print("对不起，您机会用完了，没有猜对")
        else:
            print("对不起，您机会用完了，没有猜对")