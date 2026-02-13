name = "SUNSET"
stock_price = 123
stock_code = 114514
stock_price_daily_growth_factor = 1.1
growth_days = 10

print(f"公司:{name},股票代码:{stock_code},当前股价:{stock_price}")
print("每日增长系数是:%s,经过%s天的增长之后,股价来到了:%.2f" % (stock_price_daily_growth_factor,growth_days,(stock_price * stock_price_daily_growth_factor ** growth_days)))

