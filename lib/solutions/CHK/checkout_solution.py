
"""
Our price table and offers:
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
import re

BASE_PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
}


class CheckoutSolution:

    def calculate_a_total(self, count):
        return (count // 5) * 200 + ((count % 5) // 3) * 130 + (count % 3) * BASE_PRICES['A']
    
    def calculate_e_total_and_b_free_count(self, count):
        # for every 2 E's, get one B free
        free_b_count = count // 2
        return count * BASE_PRICES['E'], free_b_count

    # skus = unicode string
    def checkout(self, skus):

        if skus is None or skus == '':
            return 0
        
        pattern = re.compile(r'^[ABCDE]+$')  # or r'^[ABCD]*$' to allow empty
        if not pattern.fullmatch(skus):
            return -1
        # this means only ABCD will count toward total
        
        a_count = skus.count('A')
        b_count = skus.count('B')
        c_count = skus.count('C')
        d_count = skus.count('D')
        e_count = skus.count('E')

        a_total = self.calculate_a_total(a_count)
        c_total = c_count * BASE_PRICES['C']
        d_total = d_count * BASE_PRICES['D']
        e_total, b_free_count = self.calculate_e_total_and_b_free_count(e_count)

        # has to be calculated after getting free B count from E's
        if b_count > 0:
            b_count -= b_free_count
        b_total = (b_count // 2) * 45 + (b_count % 2) * BASE_PRICES['B']

        return sum([a_total, b_total, c_total, d_total, e_total])
