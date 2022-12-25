import pathlib

# Работаем с папкой resources


def read_data(file: str):
    with open(file, 'r') as f:
        return f.readlines()


def write_data(file: str, data):
    with open(file, 'w') as f:
        f.writelines(data)


def remove_comments(source_file: str, target_file: str):
    source_file = read_data(source_file)
    for line in source_file:
        if '#' in line:
            source_file.remove(line)
    write_data(target_file, source_file)


if __name__ == "__main__":
    resource_path = pathlib.Path(
        __file__).parent.resolve() / 'resources'
    source_file_name = input('Введите название исходного файла: ')
    target_file_name = input('Введите имя целевого файла: ')

    source_file_path = resource_path / source_file_name
    target_file_path = resource_path / target_file_name
    if source_file_path.is_file():
        remove_comments(source_file_path, target_file_path)
    else:
        print('Исходного файла не существует :(')
