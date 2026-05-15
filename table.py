from column import Column

class Table:
    def __init__(self, table_id: str, table_name: str, columns: list):
        self.table_name: str = table_name.replace(' ', '_')
        self.table_id = table_id
        
        self.columns: list = []
        self.foreign_keys: list = []
        self.get_columns(columns)
        
    def get_columns(self, columns: list) -> list:
        cols: list = [Column(column) for column in columns]
        for c in cols:
            if c.foreign_columns:
                self.foreign_keys.append(c)
            else:
                self.columns.append(c)