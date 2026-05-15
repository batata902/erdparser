import random

def random_chars() -> str:
    chars: str = 'abcdefghijklmnopqrstuvwxyz'
    pre_random: list = [random.choice(chars)] * 5

    return "".join(pre_random)    