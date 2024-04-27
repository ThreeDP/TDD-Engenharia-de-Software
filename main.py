import unittest

def add(x, y):
    try:
        if isinstance(x, str) and isinstance(float(x), float):
            x = float(x)
        if isinstance(y, str) and isinstance(float(y), float):
            y = float(y)
    except:
        return "variable no numeric"
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    if x.isdigit() and y.isdigit():
        return x * y

def div(x, y):
    return x / y


class Test_add(unittest.TestCase):

    def test_add_two_positive_numbers_5_and_6(self):
        self.assertEqual(add(5, 6), 11)
    
    def test_add_two_negative_numbers_minus_5_and_minus_6(self):
        self.assertEqual(add(-5, -6), -11)
    
    def test_add_two_zeros(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_two_words_a_b(self):
        self.assertEqual(add('ab', 'br'), "variable no numeric")

    def test_pass_a_float_and_a_int_number(self):
        self.assertEqual(add(3.1, 5), 8.1)

    def test_pass_a_numeric_str_and_a_int_number(self):
        self.assertEqual(add("3", 5), 8)

    def test_pass_a_numeric_str_and_a_int_number(self):
        self.assertEqual(add("3.1", 5), 8.1)

    def test_pass_double_signal_minus_in_values(self):
        self.assertEqual(add("--3.1", -5), "variable no numeric")



if __name__ == '__main__':
    unittest.main()