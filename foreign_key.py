class ForeignKey:
    def __init__(self, name: str, columns: list):
        self.name: str = name
        self.columns: list = columns
        self.sourceTableId: str = self.getSourceTableId(self.columns)

    def getSourceTableId(self, atributes: list) -> str:
        id: str = ''
        for a in atributes:
            try:
                id = a['sourceTableId']
            except KeyError:
                continue

        return id

    def get_fkey_column(self) -> str:
        return self.name
    
    def get_fkey_referenceId(self) -> str:
        return self.sourceTableId
    
    def get_attr(self) -> str:
        for a in self.columns:
            return a['name']
        return 'NULL'