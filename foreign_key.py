from compiler.utils import parse_type

class ForeignKey:
    def __init__(self, column: dict, sourceTableId: str):
        self.name: str = column.get('name', '')
        self.type: str = column.get('type', '')

        self.sourceTableId: str = sourceTableId
    

    def get_fk_source_table(self, column: dict) -> list:
        foreign_key_refs: list = column['foreignKeyProps']['columns'] # [ {name: 'fk_example', type='char{n}', size='11'}, {...}, {...} ]
        self.sourceTableId = column['foreignKeyProps']['sourceTableId']

        for f_ref in foreign_key_refs:
            f_ref.pop('id')

            f_ref['type'] = parse_type(f_ref)

        return foreign_key_refs
    