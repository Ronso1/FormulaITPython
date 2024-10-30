money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

count_month = 0
# Строки 8 и 9 рассчитывают первый месяц без начисления процента на расходы
money_capital += salary
money_capital -= spend

while money_capital > 0:
    spend = spend * (1 + increase)
    money_capital += salary - spend
    count_month += 1

print("Количество месяцев, которое можно протянуть без долгов:", count_month)