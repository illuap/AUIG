import win32gui

from src.ImageGrabber.ScreenGrabber import ScreenGrabberWin32


class CursorRelativePosition:

    @staticmethod
    def get_relative_cursor_position() -> (int, int):
        # Gets cursor relative to nox window.
        sg = ScreenGrabberWin32("NoxPlayer")
        window_cord = sg.getWindowPosition()
        cursor_cord = win32gui.GetCursorPos()

        return cursor_cord[0] - window_cord[0],  cursor_cord[1] - window_cord[1]
