from table import Table

class SchemaMaker:
    def __init__(self, tables: list):
        self.tables: list = tables
        self.schema: str = self.create_db(self.tables)


    def save_file(self, file_name: str):
        open(file_name, 'w', encoding='utf-8').write(self.schema)
        print(f'[+] Schema criado --> {file_name}')


    def create_db(self, tables: list) -> str:
        schema: str = ''
        for t in tables:
            schema += self.create_table(t.table_name, t.columns)
        return schema


    def create_table(self, table_name: str, cols: list) -> str:
        sql_line: str = f'CREATE TABLE IF NOT EXISTS {table_name} (\n{self.create_columns(cols)});\n\n'
        return sql_line


    def create_columns(self, cols: list) -> str:
        final_columns_text: str = ''
        for c in cols:
            final_columns_text += f'\t{c.name} {'NULL' if c.metadata.get('type', False) is False else c.metadata['type']}'
            if c.metadata['isPkey']:
                final_columns_text += ' PRIMARY KEY'
            final_columns_text += ',\n'
        return final_columns_text
        