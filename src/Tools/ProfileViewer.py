
import os


class ProfileViewer():


    def GetAllProfiles():
        f = os.listdir("./data")

        return f

    def CheckIfProfileExistsInRoot(fileName):
        return os.path.exists(fileName)

    def CheckIfProfileExistsInDataFolder(fileName):
        return os.path.exists(fileName)

    def GetFileDirForDataFile(fileName):
        if(os.path.exists("./data/"+fileName)):
            return "./data/"+fileName
        if(os.path.exists("./"+fileName)):
            return "./"+fileName
        if(os.path.exists(fileName)):
            return fileName
            
        raise Exception()