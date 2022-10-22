import unittest
from main import *
from formulas import *

def is_within_percentage_diff(value, desired_value, max_difference):
    percent_of_desired_value = ((value / desired_value) * 100)
    if abs((100 - percent_of_desired_value)) <= max_difference:
        print(f"OKAY, value is {percent_of_desired_value}% of desired value")
        return True
    else:
        print(f"WRONG, value is {percent_of_desired_value}% of desired value, max difference is {max_difference}")

def is_within_diff(value, desired_value, diff_by_percantage_of_desired_value):
    real_difference = abs(desired_value - value)

    if ((value < desired_value) and (value + desired_value*diff_by_percantage_of_desired_value >= desired_value)) or ((value > desired_value) and (value + desired_value*diff_by_percantage_of_desired_value <= desired_value)):
        print(f"OKAY, max allowed difference is {desired_value*diff_by_percantage_of_desired_value}, real difference is {real_difference}")
        return True

    else:
        print(f"WRONG, max allowed difference is {desired_value*diff_by_percantage_of_desired_value}, real difference is {real_difference}")
        return False


class TestMain(unittest.TestCase):
 
    def test_get_orbital_period(self):
        self.assertAlmostEqual(get_orb_period(600000 +  planets["earth"]["radius"] , "earth"), 5801, None, None, 100)
        self.assertAlmostEqual(get_orb_period(450000000 +  planets["earth"]["radius"] , "earth"), 3068302.68, None, None, 1000)
        self.assertAlmostEqual(get_orb_period(400000 +  planets["earth"]["radius"] , "earth"), 5553.63, None, None, 100)

    def test_get_semimajor_axis(self):
        self.assertEqual(round(get_semimajor_axis(5802.289, "earth") -  planets["earth"]["radius"], -2),600000)
        self.assertEqual(round(get_semimajor_axis(3068302.68, "earth") -  planets["earth"]["radius"] , -7),450000000, None)
        self.assertEqual(round(get_semimajor_axis(5553.63, "earth") -  planets["earth"]["radius"] , -4),400000)
    
    def test_new_test_function(self):
        is_within_diff(10,15,0.50)
        is_within_diff(10,15,0.20)

if __name__ == '__main__':
    unittest.main()
