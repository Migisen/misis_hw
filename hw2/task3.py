def task_3() -> None:
    word = 'объектно-ориентированный'
    object_ = word[:6]
    orient = word[9:17]
    tir = word[14:17]
    kot = word[4:16:5]
    renta = word[10:14:2] + word[13:15] + word[19]
    print(object_, orient, tir, kot, renta)


if __name__ == '__main__':
    task_3()
