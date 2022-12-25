import zipfile
import pathlib
import io

from collections import Counter


def read_text_from_zip(file: str, name: str):
    with zipfile.ZipFile(file, 'r') as z:
        with io.TextIOWrapper(z.open(name), encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    # Можно не убирать, но пусть будет
                    yield line.strip('\n').strip()


if __name__ == "__main__":
    path_to_file = pathlib.Path(
        __file__).parent.resolve() / 'resources' / 'voyna-i-mir.zip'
    result = Counter()
    for data in read_text_from_zip(path_to_file, 'voyna-i-mir.txt'):
        result += Counter(data)
    save_path = pathlib.Path(
        __file__).parent.resolve() / 'resources' / 'voyna-i-mir.counted'

    most_common_letters = result.most_common()
    most_common_letters.reverse()
    with open(save_path, 'w') as f:
        f.write('\n'.join('{} {}'.format(
            x[0], x[1]) for x in most_common_letters))
