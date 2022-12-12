from typing import Iterator, Optional, Union


def flatten_dict(target_dict: dict, depth: Optional[int] = None, iteration_result: tuple = ()) -> Iterator[dict]:
    # По аналогии с задачей 1
    for key, value in target_dict.items():
        if not isinstance(value, dict):
            yield iteration_result + (key, value)
        else:
            if depth is None:
                yield from flatten_dict(value, depth, iteration_result + (key,))
            else:
                if depth == 0:
                    yield iteration_result + (key, value)
                else:
                    yield from flatten_dict(value, depth - 1, iteration_result + (key, ))


def access_value_by_path(target_dict: dict, path: tuple):
    for path_item in path:
        target_dict = target_dict[path_item]
    return target_dict


def serach_dict(target_dict: dict, search_key: Union[str, int], depth: Optional[int] = None):
    for item in flatten_dict(target_dict, depth=depth):
        if search_key in item:
            path_to_value = item[:item.index(search_key)+1]
            print(f'Путь до ключа: {path_to_value}')
            target_value = access_value_by_path(target_dict, path_to_value)
            print(
                f'Значение ключа: {target_value}')
            return target_value

    print('Ничего не нашли')
    return None


if __name__ == "__main__":
    site = {
        'html': {
            'head': {
                'title': 'Мой сайт'
            },
            'body': {
                'h2': 'Здесь будет мой заголовок',
                'div': 'Тут, наверное, какой-то блок',
                'p': 'А вот здесь новый абзац'
            }
        }
    }
    search_key = input('Введите искомый ключ: ')
    use_depth = input('Хотите ввести максимальную глубину? Y/N: ')
    if use_depth == 'Y':
        search_depth = int(input('Введите максимальную глубину: '))
    else:
        search_depth = None
    serach_dict(site, search_key, search_depth)
