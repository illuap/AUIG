import os
import shutil

from src.Actions.ActionProfileModel import ActionProfileModel


class ActionValidation:

    @staticmethod
    def validate_new_action(action: ActionProfileModel) -> ActionProfileModel:
        corrected = action

        # Should validate all the images by reorganizing them to the local folder.
        for i, img in enumerate(corrected.images):
            corrected.images[i] = ActionValidation.__organize_img(img)

        return corrected

    @staticmethod
    def __organize_img(img_dir: str) -> str:
        if ActionValidation.__is_internal_img_dir(img_dir):
            print("do something here")
            return img_dir
        elif not os.path.exists(img_dir):
            raise FileNotFoundError
        else:
            new_img_dir = ActionValidation.__copy_img_to_internal_folder(img_dir)
            return new_img_dir

    @staticmethod
    def __is_internal_img_dir(img_dir: str) -> bool:

        sub_dir = "./images/"

        if img_dir[0:len(sub_dir)] == sub_dir:  # get local directory + ./images/_________________
            return True
        else:
            return False

    @staticmethod
    def __copy_img_to_internal_folder(img_dir):
        dir, filename = os.path.split(img_dir)
        sub_dir = "./images/"

        new_dir = sub_dir + filename

        # Append a number if the file already exists..
        i = 1
        while os.path.exists(new_dir):
            file, ext = os.path.splitext(filename)
            new_dir = "{0}{1}_{2}{3}".format(sub_dir, file, str(i), ext)
            i = i+1

        shutil.copyfile(img_dir, new_dir)

        if os.path.exists(new_dir):
            return new_dir
        else:
            raise
