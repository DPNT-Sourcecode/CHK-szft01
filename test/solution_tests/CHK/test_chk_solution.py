from solutions.CHK.checkout_solution import CheckoutSolution


"""
Our price table and offers:
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+
"""


class TestSum():
    def test_sum(self):

        # CHK_1
        assert CheckoutSolution().checkout('') == 0
        assert CheckoutSolution().checkout(None) == 0
        assert CheckoutSolution().checkout('A') == 50
        assert CheckoutSolution().checkout('AA') == 100
        assert CheckoutSolution().checkout('AAA') == 130
        assert CheckoutSolution().checkout('AAAA') == 180
        assert CheckoutSolution().checkout('AAAAA') == 230
        assert CheckoutSolution().checkout('AAAAAA') == 260
        assert CheckoutSolution().checkout('BB') == 45
        assert CheckoutSolution().checkout('BBB') == 75 
        assert CheckoutSolution().checkout('BBBB') == 90
        assert CheckoutSolution().checkout('CC') == 40
        assert CheckoutSolution().checkout('DD') == 30
        assert CheckoutSolution().checkout('ABCD') == 115
        assert CheckoutSolution().checkout('ABCDABAA') == 260
        assert CheckoutSolution().checkout('XYZ') == -1
        assert CheckoutSolution().checkout('ABCa') == -1
        assert CheckoutSolution().checkout('-') == -1

        # CHK_2 new tests for E and free B
        assert CheckoutSolution().checkout('E') == 40
        assert CheckoutSolution().checkout('EE') == 80
        assert CheckoutSolution().checkout('EEB') == 80  # one B free
