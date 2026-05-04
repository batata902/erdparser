from erdparser.column import Column

class Table:
    def __init__(self, table_name: str, columns: list):
        self.table_name: str = table_name
        
        self.columns: list = self.get_columns(columns)
        
    def get_columns(self, columns: list) -> list:
        return [Column(column) for column in columns]
            