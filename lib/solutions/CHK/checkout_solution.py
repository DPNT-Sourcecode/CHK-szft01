
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

# could map values to their calculation functions here TODO
BASE_PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50,
}


class CheckoutSolution:

    def calculate_a_total(self, acount):
        """3A for 130, 5A for 200"""
        five_pack_count = acount // 5
        remainder_after_five_packs = acount % 5

        return (five_pack_count) * 200 + (remainder_after_five_packs // 3) * 130 + (remainder_after_five_packs % 3) * BASE_PRICES['A']
    
    def calculate_b_total(self, bcount, bfree_count):
        """
        - has to be calculated after getting free B count from E's
        - without free B count its 2B for 45
        """
        if bcount > 0:
            bcount -= bfree_count
        b_total = (bcount // 2) * 45 + (bcount % 2) * BASE_PRICES['B']
        return b_total

    def calculate_e_total_and_b_free_count(self, ecount):
        """2E get one B free"""
        free_b_counts = ecount // 2
        return ecount * BASE_PRICES['E'], free_b_counts
    
    def calculate_f_total(self, fcount):
        """2F get one F free"""
        chargeable_f_count = fcount - (fcount // 3)
        return chargeable_f_count * BASE_PRICES['F']

    def checkout(self, skus):

        if skus is None or skus == '':
            return 0
        
        pattern = re.compile(r'^[A-Z]+$') # any capital letter
        if not pattern.fullmatch(skus):
            return -1
        # this means only capital letter will count toward total

        letter_counts = {}

        for letter in BASE_PRICES.keys():
            letter_counts[letter] = skus.count(letter)

        # cant think of a clean way to avoid these next 26 calculations
        # could assign fucntions to each letter in BASE_PRICES and rename but there are dependencies like free Bs for E aso have to do E before B
        # just gonna get it working for now

        a_total = self.calculate_a_total(letter_counts['A'])
        c_total = letter_counts['C'] * BASE_PRICES['C']
        d_total = letter_counts['D'] * BASE_PRICES['D']

        e_total, b_free_count = self.calculate_e_total_and_b_free_count(letter_counts['E'])
        b_total = self.calculate_b_total(letter_counts['B'], b_free_count)

        f_total = self.calculate_f_total(letter_counts['F'])

        
        

        return sum([a_total, b_total, c_total, d_total, e_total, f_total])


