import random

def random_chars() -> str:
    chars: str = 'abcdefghijklmnopqrstuvwxyz'
    pre_random: list = [random.choice(chars)] * 5

    return "".join(pre_random)    

def findTablebyId(self, tables: list, id: str) -> str | bool:
    for t in tables:
        if t.table_id == id:
            return t.table_name
    return False