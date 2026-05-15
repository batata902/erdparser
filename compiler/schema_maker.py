from table import Table
from compiler.utils import random_chars, findTablebyId

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
            schema += self.create_table(t.table_name, t.columns, t.foreign_keys)
        return schema


    def create_table(self, table_name: str, cols: list, fkeys: list) -> str:
        sql_line: str = f'CREATE TABLE IF NOT EXISTS {table_name} (\n{self.create_columns(cols, fkeys)});\n\n'

        if fkeys:
            fk: str = self.add_fkeys(table_name, fkeys)
            sql_line += fk if fk != None else ''
        return sql_line


    def create_columns(self, cols: list, fkeys: list) -> str:
        final_columns_text: str = ''
        for c in cols:
            if c.metadata['isPkey'] and c.metadata['type'] == 'INTEGER':
                c.metadata['type'] = 'SERIAL'
            final_columns_text += f'\t{c.name} {'NULL' if c.metadata.get('type', False) is False else c.metadata['type']}'
            if c.metadata['isPkey']:
                final_columns_text += ' PRIMARY KEY'

            if not c.metadata['isOpt'] and not c.metadata['isPkey']:
                final_columns_text += ' NOT NULL'
            final_columns_text += ',\n'

        for c in fkeys:
            for f in c.foreign_columns:
                final_columns_text += f'\t{f} {c.foreign_columns[f].columns[0]['type']},\n'
        
        final_columns_text = final_columns_text[::-1].replace(",", "", 1)[::-1]

        return final_columns_text
        

    def add_fkeys(self, table_name: str, fkeys: list) -> str:
        alter_table: str = ''
        for f in fkeys:
            for fk in f.foreign_columns:
                alter_table: str = f'ALTER TABLE {table_name} ADD CONSTRAINT {table_name + '_' + random_chars()} FOREIGN KEY({fk}) REFERENCES {findTablebyId(self.tables, f.foreign_columns[fk].sourceTableId)}({f.foreign_columns[fk].get_attr()});\n\n'
        return alter_table