from db_entities.column import Column
from db_entities.foreign_key import ForeignKey
from converter.utils import parse_type, isForeignKey

class Table:
    def __init__(self, table_id: str, table_name: str, columns: list):
        self.table_name: str = table_name.replace(' ', '_')
        self.table_id = table_id
        
        self.columns: list[Column] = []
        self.foreign_keys: list[ForeignKey] = []

        self.get_columns(columns)
        
    def get_columns(self, columns: list) -> list:
        for c in columns:
            if isForeignKey(c):
                foreign_key_infos, sourceTableId = self.get_fk_source_table_id(c)
                for fki in foreign_key_infos:
                    new_fkey: ForeignKey = ForeignKey(fki, sourceTableId)
                    self.foreign_keys.append(new_fkey)
            else:
                new_column: Column = Column(c)
                self.columns.append(new_column)

    def get_fk_source_table_id(self, column: dict) -> tuple[list , str]:
        foreign_key_refs: list = column['foreignKeyProps']['columns'] # [ {name: 'fk_example', type='char{n}', size='11'}, {...}, {...} ]
        sourceTableId = column['foreignKeyProps']['sourceTableId']

        for f_ref in foreign_key_refs:
            f_ref.pop('id')

            f_ref['type'] = parse_type(f_ref)

        return (foreign_key_refs, sourceTableId)