# POCO F1 LOGO GENERATOR
# COPYRIGHT MOHAMAD OBEID 2022
# I AM VERY SCARED THAT IT WILL BREAK MY PHONE WAHHHHHH

import os

print("-----------------------------------------------")
print("   POCOSPLASHER REMAKE FOR MIUI 12 FIRMWARE")
print("fuck you xiaomi for ruining the old masterpiece")
print("-----------------------------------------------")

# Make sure the order is correct like in the binary!!!

files = [
    "header.bin",
    "small_mi.bmp",
    "fastboot.bmp",
    "mi_unlocked.bmp",
    "system_destroyed.bmp",
    "poco.bmp",
    "poco_unlocked.bmp",
    "poco2.bmp",
    "poco2_unlocked.bmp"
]

# Exact filesizes in bytes, because its binary bro
# also order sensetive
# you dont wanna mess with that right

filesizes = [
    20480,   # header.bin
    1945600,  # small_mi.bmp
    2056192,  # fastboot.bmp
    1945600,  # mi_unlocked.bmp
    7278592,  # system_destroyed.bmp
    2334720,  # poco.bmp
    2334720,  # poco_unlocked.bmp
    2334720,  # poco2.bmp
    2334720  # poco2.bmp
]


def setLen(file, newsize):
    with open(file, mode="r+b") as b:
        b.seek(newsize - 1)
        b.write(b'\00')


def checkFile():
    # Checks for missing files or with invalid size
    # Returns false if something is wrong, and true if sucessful
    id = 0
    for file in files:
        if (os.path.isfile(file)):
            if (os.path.getsize(file) == filesizes[id]):
                print(file + ": PASS!")
            elif (os.path.getsize(file) > filesizes[id]):
                print(file + ": ERR_TOO_BIG")
                return False
            else:
                print(file + ": WARN_TOO_SMALL [FIXING]")
                setLen(file, filesizes[id])
                print(file + ": PASS!")
        else:
            print(file + ": ERR_NOT_FOUND")
            return
        id += 1
    return True


def genFile():
    out = open("logo.img", "wb")
    id = 0
    for file in files:
        try:
            with open(file, mode="rb") as rb:
                bytes = rb.read()
            out.write(bytes)
            print(file + ": written to final logo.img")
        except Exception as e:
            print("Oh boy something crashed! Send this to the developer now!")
            print(e)
            return False
        id += 1
    print("Final touches ...")
    out.close()
    print("Saved final logo.img!")
    return True


if (checkFile()):
    print("File checking pass!")
    print("-------------------")
    print("Generating logo.img ...")
    if (genFile()):
        print("You can now cross your fingers and flash it with fastboot :D")
    else:
        print("Do NOT flash this file!")
else:
    print("File checking fail!")
