import os

import jsonpickle


class FileGenerator:

    @staticmethod
    def GenerateCopyOfFile(fileName) -> str:
        base_json_file = ""
        newDir, newFile = os.path.split(fileName)
        standAloneName, extension = os.path.splitext(newFile)
        count = 0

        exists = True
        while exists:
            newFile = newDir + "/" + standAloneName + "_" + str(count) + extension
            if not os.path.exists(newFile):
                exists = False
            else:
                count = count + 1

        with open(fileName, 'r') as f:
            base_json_file = jsonpickle.decode(f.read())
        with open(newFile, 'w+') as f:
            f.write(jsonpickle.encode(base_json_file, unpicklable=False))
            f.close()

        return newFile
