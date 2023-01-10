class APIError(Exception):

    def __init__(self, message, code):
        self.errorCode = code
        self.message = message
        super().__init__(self.message)

class InvalidClanQuery(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
