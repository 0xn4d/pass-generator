import random, string

print('')
size = int(input('tell me the size of password that you want: '))
print('')

chars = string.ascii_letters + string.digits + '!@#$%&*()-=+;:/?'

rnd = random.SystemRandom()

print('-' * 35)
print(''.join(rnd.choice(chars) for i in range(size)))
print('-' * 35)
