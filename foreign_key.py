class ForeignKey:
    def __init__(self, name: str, columns: dict):
        self.name = name
        self.columns = columns
        self.sourceTableId = self.columns['sourceTableId']

    def get_fkey_column(self) -> str:
        return self.name
    
    def get_fkey_referenceId(self) -> str:
        return self.sourceTableId