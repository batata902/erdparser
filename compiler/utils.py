import random

def random_chars() -> str:
    chars: str = 'abcdefghijklmnopqrstuvwxyz'
    pre_random: list = []

    for i in range(0, 5):
        pre_random.append(random.choice(chars))

    return "".join(pre_random)    

def findTablebyId(tables: list, id: str) -> str | bool:
    for t in tables:
        if t.table_id == id:
            return t.table_name
    return False