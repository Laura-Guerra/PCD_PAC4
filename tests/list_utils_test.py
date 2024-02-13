from utils import list_utils


def operate(num, plus_num, for_num):
    return num + plus_num * for_num


class ListUtilsTestCase:
    def test_apply_function_to_list(self):
        lst = [1, 2, 3, 4, 5]
        result = list_utils.apply_function_to_list(operate, lst,
                                                   plus_num=2, for_num=5)
        assert result == [11, 12, 13, 14, 15]

    def test_print_list(self):
        lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']
        assert list_utils.print_list(lst) is None

    def test_print_list_with_n(self):
        lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']
        assert list_utils.print_list(lst, 3) is None

    def test_print_list_negative_n(self):
        lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']
        assert list_utils.print_list(lst, -2) is None
