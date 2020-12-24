from src.WebApp.Types.ResultCode import ResultCode


class ResultStatus:
    Code: ResultCode = None
    Message: str = ""
    Data = None

    def __init__(self, code, message, data = None):
        self.Code = code
        self.Message = message
        self.Data = data

    def get_js_message(self):
        return self.Code, self.Message, self.Data
