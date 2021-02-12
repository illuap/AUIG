
import os


class ProfileViewer():


    def GetAllProfiles(self):
        f = os.listdir("./data")

        return f

    def CheckIfProfileExistsInRoot(fileName):
        return os.path.exists("./"+fileName)

    def CheckIfProfileExistsInDataFolder(fileName):
        return os.path.exists("./data/"+fileName)

    def GetFileDirForDataFile(fileName):
        if(os.path.exists("./data/"+fileName)):
            return "./data/"+fileName
        if(os.path.exists("./"+fileName)):
            return "./"+fileName
        if(os.path.exists(fileName)):
            return fileName

        raise OSError(2, "Could not file in the data folder", fileName)