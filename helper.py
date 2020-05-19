def convertJStoPYFileName(s):
    result = s.replace("\\", "/")
    result = "./web" + result
    return result
