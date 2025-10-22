
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
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+
"""
import re

BASE_PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
}


class CheckoutSolution:

    def calculate_a_total(self, acount):
        # i need the remainder here instead of just count %3

        five_pack_count = acount // 5
        remainder_after_five_packs = acount % 5

        return (five_pack_count) * 200 + (remainder_after_five_packs // 3) * 130 + (remainder_after_five_packs % 3) * BASE_PRICES['A']
    
    def calculate_e_total_and_b_free_count(self, ecount):
        # for every 2 E's, get one B free
        free_b_count = ecount // 2
        return ecount * BASE_PRICES['E'], free_b_count
    
    def calculate_f_total(self, fcount):
        # for every 2 F's, get one F free
        chargeable_f_count = fcount - (fcount // 3)
        return chargeable_f_count * BASE_PRICES['F']

    # skus = unicode string
    def checkout(self, skus):

        if skus is None or skus == '':
            return 0
        
        pattern = re.compile(r'^[ABCDEF]+$')  # or r'^[ABCD]*$' to allow empty
        if not pattern.fullmatch(skus):
            return -1
        # this means only ABCD will count toward total
        
        a_count = skus.count('A')
        b_count = skus.count('B')
        c_count = skus.count('C')
        d_count = skus.count('D')
        e_count = skus.count('E')
        f_count = skus.count('F')

        a_total = self.calculate_a_total(a_count)
        c_total = c_count * BASE_PRICES['C']
        d_total = d_count * BASE_PRICES['D']
        e_total, b_free_count = self.calculate_e_total_and_b_free_count(e_count)
        f_count = self.calculate_f_total(f_count)

        # has to be calculated after getting free B count from E's
        if b_count > 0:
            b_count -= b_free_count
        b_total = (b_count // 2) * 45 + (b_count % 2) * BASE_PRICES['B']

        return sum([a_total, b_total, c_total, d_total, e_total, f_count])


