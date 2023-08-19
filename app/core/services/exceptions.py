class GenericError(Exception):
    def __init__(self, error: str):
        super().__init__(error)
        self.code = error

    def as_dict(self):
        return {"code": self.code}
