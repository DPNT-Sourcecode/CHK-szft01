from solutions.CHK.checkout_solution import CheckoutSolution


"""
Our price table and offers:
CHK1
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+

CHK2
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+
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
        # assert CheckoutSolution().checkout('AAAAA') == 230
        # assert CheckoutSolution().checkout('AAAAAA') == 260
        # as of CHK_2 theres a discount for 5A for 200
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
        assert CheckoutSolution().checkout('AAAAA') == 200
        assert CheckoutSolution().checkout('AAAAAA') == 250
        assert CheckoutSolution().checkout('AAAAAAAAA') == 380  # 1x200(5), 1x130(3), 1x50(1)
        assert CheckoutSolution().checkout('EEEEBB') == 160
        assert CheckoutSolution().checkout('AAAEEBB') == 240

        # CHE_3
        assert CheckoutSolution().checkout('F') == 10
        assert CheckoutSolution().checkout('FF') == 20
        assert CheckoutSolution().checkout('FFF') == 20
        assert CheckoutSolution().checkout('FFFF') == 30
        assert CheckoutSolution().checkout('FFFFF') == 30