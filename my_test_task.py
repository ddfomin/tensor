# В магазине акция: «купи три одинаковых товара и заплати только за два».
# Конечно, каждый купленный товар может участвовать лишь в одной акции. Акцию можно использовать многократно.
# Например, если будут куплены 7 товаров одного вида по цене 2 за штуку и 5 товаров другого вида по цене 3 за штуку,
# то вместо 7 * 2 + 5 * 3 надо будет оплатить 5 * 2 + 4 * 3 = 22.
# Считая, что одинаковые цены имеют только одинаковые товары, найдите сумму к оплате.
# Входные данные для функции main: Список цен товаров разделенной пробелами
# Выходные данные: Сумма к оплате

def main(n):
    numbers = n.split()
    numbers = [int(n) for n in numbers]

    result = {}
    for num in numbers:
        result[num] = result.get(num, 0) + 1
    key = [value for value in result.keys()]

    value = [value for value in result.values()]
    value_correct = [n - int(n / 3) for n in value]

    answer = []
    for i in range(len(key)):
        answer.append(key[i] * value_correct[i])

    return sum(answer)


data = [
    '2 2 2 2 2 2 2 3 3 3 3 3',
    '2 3 2 3 2 2 3 2 3 2 2 3',
    '10000',
    '1 2 3 1 2 3 1 2 3',
    '10000 10000 10000 10000 10000 10000',
    '300 100 200 300 200 300'
]
test_data = [22, 22, 10000, 12, 40000, 1100]

for i, d in enumerate(data):
    res = main(d)
assert res == test_data[i], f'{res}, {test_data[i]}, {i}'
