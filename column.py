from foreign_key import ForeignKey

class Column:
    def __init__(self, column: dict):
        self.id: str = column['id']
        self.name: str = column['name'].replace(' ', '_')

        self.foreign_columns: dict = {}
        self.metadata: dict = {}
        self.parse_metadata(column)

    def parse_metadata(self, columns: dict):
            is_fkey: bool = columns.get('isForeignKey', False)
            if is_fkey:
                self.save_fkey(ForeignKey(self.name, self.get_fk_props(columns)))
                return
            
            self.metadata = {
                'type': self.parse_type(columns),
                'isPkey': columns.get('isPrimaryKey', False), 
                'itsOpt': columns.get('itsOptional', False), 
                'isUniq': columns.get('isUnique', False)
            }
    
    def save_fkey(self, f_key: ForeignKey | None):
        self.foreign_columns[f_key.name] = f_key
    
    def get_fk_props(self, column: dict) -> list:
        foreign_key_refs: list = column['foreignKeyProps']['columns']
        for f_ref in foreign_key_refs:
            f_ref.pop('id')
        return foreign_key_refs

    def parse_type(self, columns: dict) -> str:
        type = columns.get('type', None)
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
