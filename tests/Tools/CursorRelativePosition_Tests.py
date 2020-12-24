import unittest
from src.Tools.CursorRelativePosition import CursorRelativePosition


class CursorRelatedPosition_Tests(unittest.TestCase):
    def test_get_relative_cursor_position(self):
        results = CursorRelativePosition.get_relative_cursor_position()
        print(results)
        self.assertIsNotNone(results)
