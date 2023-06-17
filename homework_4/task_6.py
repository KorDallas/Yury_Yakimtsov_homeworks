price = 100000
bank = int(input("Укажите ваш баланс:" ))
p_diff = 0
if bank >= price:
    bank = bank - price
    print(f"Поздравляю, вы купили автомобиль! Остаток на вашем счету {bank} рублей.")
else:
    p_diff = price - bank
    print(f'У вас недостаточно средств для покупки автомобиляю На счету {bank} рублей, нехватает {p_diff} рублей')
print("Хорошего дня!")