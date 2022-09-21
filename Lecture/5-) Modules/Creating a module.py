"""
Modüller konusu
"""

"""
Kullanmak için 3 yol var
"""

'---------------------------------'

'1. yol = import.modul_adi'
import math

print(dir(math))
print(help(math))

print(math.sqrt(25))
print(math.cosh(60))

'--------------------------------'

'2. yol = from modul_adi import * (icindeki tüm fonksiyonları dahil eder)'
from math import *

print(factorial(5))
print(floor(6.4))

'----------------------------------'

'3. yol = from modul_adi import kullanicaklarimiz (sectiklerimizi aktif eder)'

from math import floor,factorial

print(floor(6.4))