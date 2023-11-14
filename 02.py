name = "煎饼集团"
stock_price = 725
stock_code = 1121
stock_daily_growth = 1.35
print("%.7f" % (stock_daily_growth))
growth_days = 59
print("%d" % growth_days)
result = stock_price * (1 + stock_daily_growth) * growth_days
print(f"stock\'s name is {name},code is {stock_code},股票价格现在是:{result:.2f}")
print("每日增长系数是：%.2f,经过%d天的增长，价格为：%.2f" % (stock_daily_growth,growth_days,result))
print(f"stock's name is {name}, code is {stock_code}, 股票价格现在是: {stock_price * (1 + stock_daily_growth) * growth_days}")

