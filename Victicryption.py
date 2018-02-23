def alpha():
    letters = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
    k = eval(input("Encode: "))
    i = list(k)
    n = []
    for x in range(len(i)):
        n.append(letters[i[x]])
    print(n)

def dealpha():
    ab = list("abcdefghijklmnopqrstuvwxyz")
    i = list((eval(input("Decode: "))))
    n = []
    for x in range(0, len(i)):
        n.append(ab[i[x]])
    print(("".join(n)))

def encrypt():
    ee = list([])
    e = list(eval(input("Encrypt: ")))
    e.append(0)
    ee.append(e[0])
    for x in range(0, (len(e) - 2)):
        ee.append((e[x] + e[x + 1]) % 25)
    print(ee)

def decrypt():
    ee = list([])
    e = list(eval(input("Decrypt: ")))
    e.append(0)
    ee.append(e[0])
    ee.append((e[1 + 1] - e[1] % 25))
    for x in range(1, (len(e) - 2)):
        if (e[x + 1] - ee[x] % 25) < 0:
            ee.append((e[x + 1] - ee[x] % 25) + 25)
        else:
            ee.append((e[x + 1] - ee[x] % 25))
    print(ee)

while True:
    t = int(eval(input("0 for Decoding, 1 for Encoding, 2 for Encryption, 3 for Decryption: ")))
    if t == 0:
        dealpha()
    elif t == 1:
        alpha()
    elif t == 2:
        encrypt()
    elif t == 3:
        decrypt()
    else:
        print("none")


7,  4, 11, 11,  14, 22, 14, 17, 11, 3

7, 11, 15, 22,   0, 11, 11,  6,  3, 14

7,  4,   4, 7, -22, 11,  0, -5, -3, 11
