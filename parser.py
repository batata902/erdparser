import json

from erdparser.table import Table

class DiagramParser:
    def __init__(self, file_path: str):
        self.file_path: str = file_path
        self.parsed_content: dict = self.parse_raw_diagram(self.file_path)
        self.nodes: list = self.parsed_content['data']['nodes']
        self.tables: list = []

    def parse_raw_diagram(self, path: str) -> dict:
        raw_content: str = open(path, 'r', encoding='utf-8').read()
        
        parsed_content: dict = json.loads(raw_content)
        return parsed_content
    
    def parse(self):
        for n in self.nodes:
            table: Table = Table(n['data']['label'], n['data']['columns'])
            self.tables.append(table)

        return self

    def get_all_tables(self) -> list:
        tables: list = self.tables
        if len(tables) == 0:
            self.parse()

        return self.tables
    