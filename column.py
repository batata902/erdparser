class Column:
    def __init__(self, column: dict):
        self.id: str = column['id']
        self.name: str = column['name']

        self.metadata: dict = self.parse_metadata(column)

    def parse_metadata(self, columns: dict) -> dict:
            ref_cols: dict = None
            if columns.get('isForeignKey', False):
                ref_cols = {'columns': self.get_fk_props(columns)}
            return {
                'type': columns.get('type', None),
                'foreignKey': ref_cols,
                'isPkey': columns.get('isPrimaryKey', False), 
                'itsOpt': columns.get('itsOptional', False), 
                'isUniq': columns.get('isUnique', False)
            }
    
    def get_fk_props(self, column: dict) -> list:
        foreign_key_refs: list = column['foreignKeyProps']['columns']
        for f_ref in foreign_key_refs:
            f_ref.pop('id')
        return foreign_key_refs

