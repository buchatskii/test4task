import dz4_4
from sys import argv

try:
    currency_number = argv[1]
    kod = str.upper(currency_number)
    try:
        massive = dz4_4.currency_rates(kod)
        print(massive[0], massive[1])
    except:
        print("None")
except IndexError:
    print("No, please")

