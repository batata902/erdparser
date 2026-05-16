from compiler.utils import parse_type

class Column:
    def __init__(self, column: dict):
        self.id: str = column['id']
        self.name: str = column['name'].replace(' ', '_')

        self.metadata: dict = {}
        self.parse_metadata(column)


    def parse_metadata(self, columns: dict):
            self.metadata = {
                'type': parse_type(columns),
                'isPkey': columns.get('isPrimaryKey', False), 
                'isOpt': columns.get('isOptional', False), 
                'isUniq': columns.get('isUnique', False)
            }
