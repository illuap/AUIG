from src.WebApp.Types.ResultCode import ResultCode


class ResultStatus:
    Code: ResultCode = None
    Message: str = ""

    def __init__(self, code, message):
        self.Code = code
        self.Message = message

    def get_js_message(self):
        return (self.Code, self.Message)
