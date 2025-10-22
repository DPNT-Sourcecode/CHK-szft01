
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


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):

        if skus is None:
            return 0
        
        a_count = skus.count('A')
        b_count = skus.count('B')
        c_count = skus.count('C')
        d_count = skus.count('D')

        a_total = (a_count // 3) * 130 + (a_count % 3) * 50
        b_total = (b_count // 2) * 45 + (b_count % 2) * 30
        c_total = c_count * 20
        d_total = d_count * 15

        return sum([a_total, b_total, c_total, d_total])



