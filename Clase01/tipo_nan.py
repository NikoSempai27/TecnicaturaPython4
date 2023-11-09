import math
from decimal import Decimal

# NaN
a = float('nan')
print(f'a: {a}')

# Modulo math
a = float('nan')
print(f'Es de tipo nan?: {math.isnan(a)}')

# Modulo decimal
a = Decimal('NaN')
print(f'Es de tipo nan?: {math.isnan(a)}')

