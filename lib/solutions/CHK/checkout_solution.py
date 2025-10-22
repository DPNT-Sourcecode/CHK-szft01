
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

# OK at the risk of taking loads of time I'm going for a big refactor - worked quite well!
# still could do more but gonna plough on for now
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

FREE_OTHER_PROUDCTS = {
    'E': 'B',
    'N': 'M',
    'R': 'Q',
}

def calculate_a_total(acount):
    """3A for 130, 5A for 200"""
    print(f"DAVE CALC A {acount}")
    five_pack_count = acount // 5
    remainder_after_five_packs = acount % 5

    return (five_pack_count) * 200 + (remainder_after_five_packs // 3) * 130 + (remainder_after_five_packs % 3) * BASE_PRICES['A']

def calculate_b_total(bcount, bfree_count=0):
    """
    - has to be calculated after getting free B count from E's
    - without free B count its 2B for 45
    """
    if bcount > 0:
        bcount -= bfree_count
    b_total = (bcount // 2) * 45 + (bcount % 2) * BASE_PRICES['B']
    return b_total

def calculate_e_total_and_b_free_count(ecount):
    """2E get one B free"""
    free_b_counts = ecount // 2
    return ecount * BASE_PRICES['E'], free_b_counts

def calculate_f_total(fcount):
    """2F get one F free"""
    chargeable_f_count = fcount - (fcount // 3)
    return chargeable_f_count * BASE_PRICES['F']

def calculate_h_total(hcount):
    """5H for 45, 10H for 80"""
    ten_pack_count = hcount // 10
    remainder_after_ten_packs = hcount % 10
    return (ten_pack_count) * 80 + (remainder_after_ten_packs // 5) * 45 + (remainder_after_ten_packs % 5) * BASE_PRICES['H']

def calculate_k_total(kcount):
    """TODO"""
    pass
def calculate_n_total(ncount):
    """TODO"""
    pass
def calculate_p_total(pcount):
    """TODO"""
    pass
def calculate_q_total(qcount):
    """TODO"""
    pass
def calculate_r_total(rcount):
    """TODO"""
    pass
def calculate_u_total(ucount):
    """TODO"""
    pass
def calculate_v_total(vcount):
    """TODO"""
    pass

PRODUCT_OFFERS = {
    'A': calculate_a_total,
    'B': calculate_b_total,
    'C': lambda c: c * BASE_PRICES['C'],
    'D': lambda c: c * BASE_PRICES['D'],
    'E': calculate_e_total_and_b_free_count,
    'F': calculate_f_total,
    'G': lambda c: c * BASE_PRICES['G'],
    'H': calculate_h_total,
    'I': lambda c: c * BASE_PRICES['I'],
    'J': lambda c: c * BASE_PRICES['J'],
    'K': calculate_k_total,
    'L': lambda c: c * BASE_PRICES['L'],
    'M': lambda c: c * BASE_PRICES['M'],
    'N': calculate_n_total,
    'O': lambda c: c * BASE_PRICES['O'],
    'P': calculate_p_total,
    'Q': calculate_q_total,
    'R': calculate_r_total,
    'S': lambda c: c * BASE_PRICES['S'],
    'T': lambda c: c * BASE_PRICES['T'],
    'U': calculate_u_total,
    'V': calculate_v_total,
    'W': lambda c: c * BASE_PRICES['W'],
    'X': lambda c: c * BASE_PRICES['X'],
    'Y': lambda c: c * BASE_PRICES['Y'],
    'Z': lambda c: c * BASE_PRICES['Z'],
}

class CheckoutSolution:

    def checkout(self, skus):

        if skus is None or skus == '':
            return 0
        
        pattern = re.compile(r'^[A-Z]+$') # any capital letter
        if not pattern.fullmatch(skus):
            return -1
        # this means only capital letter will count toward total

        letter_counts = {}

        for ltr in skus:
            if ltr in letter_counts:
                letter_counts[ltr] += 1
            else:
                letter_counts[ltr] = 1

        final_total = 0

        # TODO explain
        # TODO extract?
        # if there are any cross product free items we have to do those first
        # eg if there are Es we have to calculate those first to get free Bs
        for cross_product_ltr in FREE_OTHER_PROUDCTS.keys():
            if cross_product_ltr in letter_counts:
                free_ltr = FREE_OTHER_PROUDCTS[cross_product_ltr]
                cross_product_ltr_total, free_ltr_count = PRODUCT_OFFERS[cross_product_ltr](letter_counts[cross_product_ltr])
                free_ltr_total = PRODUCT_OFFERS[free_ltr](letter_counts.get(free_ltr, 0), free_ltr_count)
                final_total += cross_product_ltr_total + free_ltr_total
                # remove these from letter_counts so they arent double counted later
                letter_counts.pop(cross_product_ltr)
                if free_ltr in letter_counts:
                    letter_counts.pop(free_ltr)

        for letter in letter_counts:
            temp = PRODUCT_OFFERS[letter](letter_counts[letter])
            final_total += temp

        return final_total



