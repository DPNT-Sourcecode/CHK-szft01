
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
        
        a_count = skus.count('A')
        b_count = skus.count('B')
        c_count = skus.count('C')
        d_count = skus.count('D')

        # the site says AI allowed, I assume using copilot is allowed in that case, massive apologies if not

        # I'm going to pause and read the page again.
        a_total = (a_count // 3) * 130 + (a_count % 3) * 50


