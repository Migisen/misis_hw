from typing import List, Optional


def generate_shop_stock(shop_list: List[list]) -> dict:
    shop_stock = {}
    for item in shop_list:
        item_name = item[0]
        item_value = item[1]
        if item_name not in shop_stock.keys():
            shop_stock[item_name] = {'total_value': item_value, 'quantity': 1}
        else:
            shop_stock[item_name]['total_value'] += item_value
            shop_stock[item_name]['quantity'] += 1
    return shop_stock


def find_in_shop(shop_stock: dict, item_name: str) -> Optional[dict]:
    # Вообще, можно было бы создать свою структуру (что-то типо ShopItem) и переопределить метод __str__
    # Но это совсем другая история
    if item_name not in shop_stock.keys():
        print('Таким товаром не торгуем :(')
        return None
    item_info = shop_stock[item_name]
    item_quantity = item_info['quantity']
    item_total_value = item_info['total_value']

    print(
        f"""
        Название детали: {item_name}
        Кол-во деталей - {item_quantity}
        Общая стоимость - {item_total_value}
        """
    )


if __name__ == '__main__':
    # Очень не нравится, что сток магазина хранится как список списков xd
    # Конвертируем в дикт (это собственно и решит задачу)

    shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], [
        'седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
    shop_stock = generate_shop_stock(shop)
    target_item = input('Что ищем?:')
    find_in_shop(shop_stock, target_item)
