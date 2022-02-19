"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

sales =   [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
product_sum_list = []

for product_dict in sales:
    items_sold = product_dict['items_sold']
    product = product_dict['product']

    sold_sum = sum(items_sold)
    product_sum_list.append(sold_sum)

    print(f'Суммарно количество продаж {product}: {sold_sum}')

all_sum = sum(product_sum_list)
print(f'Суммарное количество всех продаж: {all_sum}')

def count_sales_avg(items_sold):
    sold_sum = 0 
    for sold in items_sold:
        sold_sum +=sold
    return sold_sum / len(items_sold)

total_sum_avg = 0
for one_product in sales:
    sum_avg = round(count_sales_avg(one_product['items_sold']))
    print(f'Среднее количество продаж {one_product["product"]}: {sum_avg} ')

total_sum_avg += sum_avg
print(f'Среднее количество продаж всех товаров: {round(total_sum_avg / len(sales))}')