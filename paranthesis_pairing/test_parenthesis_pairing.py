import unittest

from parenthesis_pairing import Text

class ParenthesisPairsTestCase(unittest.TestCase):
    """Test for 'parenthesis_pairing.py'."""

    test_string_pass = Text("one((a)(two(b)))((c)(d))")
    test_string_fail1 = Text(")((this))(")
    test_string_fail2 = Text("((one)))")
    test_string_fail3 = Text("nothing")

    def test_count_parenthesis_pairs_pass(self):
        """Can it count the 7 pairs of parenthesis?"""
        self.assertEqual(self.test_string_pass.count_parenthesis_pairs(), 7)
        self.assertEqual(self.test_string_fail1.count_parenthesis_pairs(), 3)

    def test_count_parenthesis_pairs_fail(self):
        """Can it recognize unmatched pairs?"""
        self.assertEqual(self.test_string_fail2.count_parenthesis_pairs(), -1)

    def test_count_parenthesis_pairs_none(self):
        """Can if identify if there are no paris in text provided?"""
        self.assertEqual(self.test_string_fail3.count_parenthesis_pairs(), 0)

    def test_verify_parenthesis_balance_pass(self):
        self.assertTrue(self.test_string_pass.verify_parenthesis_balance())
        self.assertTrue(self.test_string_fail3.verify_parenthesis_balance(), msg="none")

    def test_verify_parenthesis_balance_fail(self):
        self.assertFalse(self.test_string_fail2.verify_parenthesis_balance(), msg="one off")
        self.assertFalse(self.test_string_fail1.verify_parenthesis_balance(), msg="Same amount")

    def test_get_list_of_parenthesis_content_pass(self):
        expected_list = [
            '(a)',
            '(b)',
            '(two(b))',
            '((a)(two(b)))',
            '(c)',
            '(d)',
            '((c)(d))'
        ]
        self.assertListEqual(self.test_string_pass.get_list_of_parenthesis_content(), expected_list)

    def test_get_list_of_parenthesis_content_fail(self):
        self.assertFalse(self.test_string_fail1.get_list_of_parenthesis_content())
        self.assertFalse(self.test_string_fail2.get_list_of_parenthesis_content())
        self.assertFalse(self.test_string_fail3.get_list_of_parenthesis_content())

if __name__ == '__main__':
    unittest.main()