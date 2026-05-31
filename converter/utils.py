import random

def random_word() -> str:
    chars: str = "abcdefghijklmnopqrstuvwxyz"
    word: str = ""
    for _ in range(0, 5):
        word += random.choice(chars)
    return word

def findTablebyId(tables: list, id: str) -> str | bool:
    for t in tables:
        if t.table_id == id:
            return t.table_name
    return False

def parse_type(columns: dict) -> str:
    type: str | None = columns.get('type', None)
    if not type:
            return None
    if 'char' in type.lower():
        try:
            size: str = columns['size']
            type = type.replace('n', size)
        except KeyError:
            pass
    if 'int' in type.lower():
            type = type.replace('INT', 'INTEGER')
    return type


def isForeignKey(column: dict) -> bool:
    is_foreign_key = column.get('isForeignKey', False)

    return is_foreign_key