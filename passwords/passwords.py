import hashlib
import binascii



words = [line.strip().lower() for line in open('words.txt')]

userauthentication = {}
database = open('passwords1.txt')

for line in database:
    jerome = line.split(':')
    user = jerome[0]
    password = jerome[1]
    userauthentication[user] = password


#answers = open('cracked1.txt', 'a')

for user in userauthentication:
    marker = user
    x = 0
    while x != 1:
        for item in words:
            phase1 = item.encode('utf-8')
            phase2 = hashlib.sha256(phase1)
            phase3 = phase2.digest()
            phase4 = binascii.hexlify(phase3)
            phase5 = phase4.decode('utf-8')
            if phase5 == userauthentication[user]:
                #answers.write(marker + ":" + item)
                print(marker + ":" + item)
                x = 1

#answers.close()