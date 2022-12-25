class NoMoneyToWithdrawError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PaymentError(Exception):
    def __init__(self, message):
        super().__init__(message)


def print_accounts(accounts):
    """Печать аккаунтов."""
    print("Список клиентов ({}): ".format(len(accounts)))
    for i, (name, value) in enumerate(accounts.items(), start=1):
        print("{}. {} {}".format(i, name, value))


def transfer_money(accounts, account_from, account_to, value):
    """Выполнить перевод 'value' денег со счета 'account_from' на 'account_to'.

    При переводе денежных средств необходимо учитывать:
        - хватает ли денег на счету, с которого осуществляется перевод;
        - перевод состоит из уменьшения баланса первого счета и увеличения
          баланса второго; если хотя бы на одном этапе происходит ошибка,
          аккаунты должны быть приведены в первоначальное состояние
          (механизм транзакции)
          см. https://ru.wikipedia.org/wiki/Транзакция_(информатика).

    Потенциальные ошибки:
        - строка 51, 52 - если там неправильный тип данных, добавление может не сработать

    Исключения (raise):
        - NoMoneyToWithdrawError: на счету 'account_from'
                                  не хватает денег для перевода;
        - PaymentError: ошибка при переводе.
    """

    try:
        process_transaction(
            accounts, account_from, account_to, value)
    except (NoMoneyToWithdrawError, PaymentError) as e:
        print(f'Ошибка при обработке перевода: {str(e)}')
        print('Изменения не применены')


def process_transaction(accounts, account_from, account_to, value) -> None:
    if accounts[account_from] < value:
        raise NoMoneyToWithdrawError('Недостаточно денег на счету')
    try:
        accounts_temp = accounts.copy()
        accounts[account_from] -= value
        accounts[account_to] += value
    except Exception as e:
        accounts = accounts_temp
        raise PaymentError(str(e))


if __name__ == "__main__":
    accounts = {
        "Василий Иванов": 100,
        "Екатерина Белых": 1500,
        "Михаил Лермонтов": 400
    }
    print_accounts(accounts)

    payment_info = {
        "account_from": "Екатерина Белых",
        "account_to": "Василий Иванов"
    }

    print("Перевод от {account_from} для {account_to}...".
          format(**payment_info))

    payment_info["value"] = int(input("Сумма = "))

    transfer_money(accounts, **payment_info)

    print("OK!")

    print_accounts(accounts)
