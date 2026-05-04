from erdparser.parser import DiagramParser
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', type=str, help='diagram path')
args = parser.parse_args()

G = '\033[32m'
B = '\033[34m'
E = '\033[m'

parser: DiagramParser = DiagramParser(args.d).parse()
tables: list = parser.tables

for t in tables:
    print(t.table_name)
    for c in t.columns:
        print(f'-> {G}column name{E} => {c.name} :: {B}column meta{E} => {c.metadata}')
