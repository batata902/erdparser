from diagram_parser.diagram_parser import DiagramParser
from converter.postgresql_converter import PostgreSQLConverter
import argparse
import sys

R = '\033[31m'
G = '\033[32m'
B = '\033[36m'
E = '\033[m'

if __name__ == '__main__':
    print('ERDPARSER v1.0')
    print('Convertendo arquivo .erdplus em .sql ...')
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--diagram', type=str, help='diagram path')
    parser.add_argument('-o', '--output', type=str, help='schema output file')
    parser.add_argument('-v', '--verbose', action='store_true', help='enable verbose')
    args = parser.parse_args()

    if not args.diagram:
        print(f'[{R}-{E}] Erro: Arquivo .erdplus não especificado!')
        sys.exit(1)
    
    output_file: str = 'schema.sql'
    if args.output:
        output_file = args.output
    else:
        print(f'[{B}INFO{E}] Arquivo de saída não específicado, criando schema com nome padrão --> {G}schema.sql{E}')

    parser: DiagramParser = DiagramParser(args.diagram).parse()
    tables: list = parser.tables

    if args.verbose:
        for t in tables:
            print(f'{G}{t.table_name}{E}')
            for c in t.columns:
                print(f'\t{G}column {E}{B}{c.name}{E}: ')
                for m in c.metadata:
                    print(f'\t\t{m}: {c.metadata[m]}')
            if t.foreign_keys:
                for c in t.foreign_keys:
                    print(f'\t\t{c.name}: {c.type} {G}Foreign_key{E}')

    schema: PostgreSQLConverter = PostgreSQLConverter(tables)
    schema.save_file(output_file)
    print(f'[{G}+{E}] Schema criado --> {G}{output_file}{E}')