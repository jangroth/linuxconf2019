counter = 0
while counter < 5:
    print(counter)
    counter += 1

for i in range(5):
    print(i)


def pfPasswordHash(arg):
    # Randomise Salt
    salt = os.urandom(6)
    # Convert String to Byte Array
    res = arg.encode()
    # Hash through 10000 times. This relates to PingFederate Algorithm 5 reference
    for lp in range(1000001):
        # Always setup hashlib. This is due to
        # the digest not resetting after .digest is called
        m = hashlib.sha256()
        # Swap between the two inputs into the digest based on loop number
        m.update(res) if lp % 2 else m.update(salt)
        m.update(salt) if lp % 2 else m.update(res)
        # Finish the digest
        res = m.digest()
    # Return the hashed result and salt in the way PingFederate is expecting
    return res.encode('base64').rstrip() + "." + salt.encode('base64').rstrip() + ".5"
