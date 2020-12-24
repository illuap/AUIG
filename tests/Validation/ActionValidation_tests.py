import os
import unittest

from src.Actions.ActionProfileModel import ActionProfileModel
from src.Validation.ActionValidation import ActionValidation


class ActionValidation_tests(unittest.TestCase):
    SAMPLE1 = ActionProfileModel(name="SAMPLE1", images=[])

    def test_validate_new_action(self):
        test_sample = self.SAMPLE1
        test_img = "C:/Users/paul/Pictures/1b2.png"
        test_sample.images.append(test_img)
        test_sample.images.append(test_img)

        results = ActionValidation.validate_new_action(test_sample)

        expected_img = "./images/1b2.png"
        expected_img_1 = "./images/1b2_1.png"

        self.assertTrue(os.path.exists(expected_img))
        self.assertEquals(results.images[0], expected_img)

        self.assertTrue(os.path.exists(expected_img_1))
        self.assertEquals(results.images[1], expected_img_1)

        os.remove(expected_img)
        os.remove(expected_img_1)
