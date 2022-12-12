def is_palindrome(target_string: str) -> bool:
    for idx in range(len(target_string)):
        if target_string[idx] != target_string[-idx-1]:
            return False
    return True


if __name__ == "__main__":
    words = ['anna', 'ne_palindrome', 'civic',
             'hannah', 'level', 'ana', 'a', 'net']
    for word in words:
        if is_palindrome(word):
            print(f'Слово "{word}" - палиндром')
        else:
            print(f'Слово "{word}" - не палиндром')
