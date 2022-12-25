from contextlib import contextmanager
import pathlib


@contextmanager
def open_or_create(name: str, mode: str):
    p = pathlib.Path(name)
    if not p.is_file() and mode in ['r', 'rb']:
        f = open(name, 'w')
    else:
        f = open(name, mode)
    try:
        yield f
    except (OSError, IOError):
        pass
    finally:
        f.close()


if __name__ == "__main__":
    path = pathlib.Path(
        __file__).parent.resolve() / 'resources' / 'test_non_existing.txt'
    with open_or_create(path, 'r') as f:
        f.write('123')
