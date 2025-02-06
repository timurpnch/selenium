import unittest


# class TestAbs(unittest.TestCase):
#     def test_abs1(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
#
#     def test_abs2(self):
#         self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"


def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"


# def test_input_text(expected_result, actual_result):
#     assert expected_result == actual_result, \
#         f'expected {expected_result}, got {actual_result}'
#
#
# def test_substring(full_string, substring):
#     assert substring in full_string, \
#         f"expected '{substring}' to be substring of '{full_string}'"


if __name__ == '__main__':
    unittest.main()
