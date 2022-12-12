def flatten_list(target_list: list):
    final_list = []
    for item in target_list:
        if isinstance(item, list):
            item = flatten_list(item)
            final_list += item
        else:
            final_list.append(item)
    return final_list


if __name__ == "__main__":
    test_list = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
    result_list = flatten_list(test_list)
    print(result_list)
