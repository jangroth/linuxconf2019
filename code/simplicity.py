counter = 0
while counter < 5:
    print(counter)
    counter += 1

for i in range(5):
    print(i)

symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]


def pfPasswordHash(arg):
    # Randomise Salt
    salt = os.urandom(6)
    # Convert String to Byte Array
    res = arg.encode()
    # Hash through 10000 times.
    for lp in range(10000):
        # Always initialize hashlib, because [...]
        m = hashlib.sha256()
        # Swap between the two inputs into the digest based on loop number
        m.update(res) if lp % 2 else m.update(salt)
        m.update(salt) if lp % 2 else m.update(res)
        # Finish the digest
        res = m.digest()
