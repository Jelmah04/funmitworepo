
import random
import string


prefix = ['TPL']
nums = random.randint(10000,99999)

def refcode():
    result = random.choice(prefix)
    return f'{result}2021{nums}'


regprefix = ['TPU']
regnums = random.randint(00000,99999)
def referrallink ():
    result = random.choice(regprefix)
    return f'{result}{nums}'
