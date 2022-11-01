from typing import List


def calculate_loans(n_friend: int, ious: int) -> List[int]:
    results = [0 for _ in range(n_friend)]
    for iou_id in range(1, ious + 1):
        print(f'{iou_id}-я расписка')
        to_whom = int(input('Кому: '))
        from_whom = int(input('От кого: '))
        how_much = int(input('Сколько??: '))
        results[to_whom - 1] -= how_much
        results[from_whom - 1] += how_much

    print('Баланс друзей')
    for friend_idx, friend_balance in enumerate(results):
        print(f'{friend_idx + 1}: {friend_balance}')
    return results


if __name__ == '__main__':
    n_friends, ious = int(input('Кол-во друзей: ')), int(input('Долговых расписок: '))
    calculate_loans(n_friends, ious)
