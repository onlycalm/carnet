class DatLenErr(Exception):
    def __init__(self):
        super().__init__("DatLenErr")

class DatFmtErr(Exception):
    def __init__(self):
        super().__init__("DatFmtErr")
