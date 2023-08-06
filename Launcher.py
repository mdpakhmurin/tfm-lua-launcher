from Protocols import IBundle

from dataclasses import dataclass

import pyautogui
import pyperclip
import time
import win32gui


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Rectangle:
    top_left: Point
    bottom_right: Point


class WindowsLauncher:
    def launch(self, bundle: IBundle):
        window_hwnd = self._get_window_hwnd("Transformice")
        rect = self._get_window_rect_without_title(window_hwnd)

        self._launch_lua(rect, bundle.get_source())

    def _get_window_hwnd(self, window_name: str) -> int:
        hwnd = win32gui.FindWindow(None, window_name)
        win32gui.SetForegroundWindow(hwnd)
        return hwnd

    def _get_window_rect_without_title(self, hwnd: int) -> Rectangle:
        window_size = win32gui.GetClientRect(hwnd)
        top_left_point = win32gui.ClientToScreen(hwnd, (window_size[0], window_size[1]))

        return Rectangle(
            Point(top_left_point[0], top_left_point[1]),
            Point(
                top_left_point[0] + window_size[2], top_left_point[1] + window_size[3]
            ),
        )

    def _launch_lua(self, window_rect: Rectangle, source_code: str) -> None:
        self._click_top_bottom_corner(window_rect)
        self._press_enter()
        self._type_text("/lua")
        self._press_enter()

        self._click_center(window_rect)
        self._select_all()
        pyperclip.copy(source_code)
        self._paste_clipboard()

        time.sleep(1)
        self._click_send_lua(window_rect)
        time.sleep(1)
        self._click_send_lua(window_rect)

    def _get_rect_center(self, rect: Rectangle) -> Point:
        return Point(
            (rect.top_left.x + rect.bottom_right.x) // 2,
            (rect.top_left.y + rect.bottom_right.y) // 2,
        )

    def _click_center(self, rect: Rectangle) -> None:
        center_point = self._get_rect_center(rect)
        pyautogui.click(center_point.x, center_point.y)

    def _click_top_bottom_corner(self, rect: Rectangle) -> None:
        x = rect.top_left.x + 10
        y = rect.top_left.y + 10

        pyautogui.click(x, y)

    def _press_enter(self) -> None:
        pyautogui.press("enter")

    def _type_text(self, text: str) -> None:
        pyautogui.write(text)

    def _select_all(self) -> None:
        pyautogui.hotkey("ctrl", "a")

    def _paste_clipboard(self) -> None:
        text = pyperclip.paste()
        pyautogui.hotkey("ctrl", "v")

    def _click_send_lua(self, rect: Rectangle) -> None:
        center_point = self._get_rect_center(rect)
        center_point.y += 40

        pyautogui.click(center_point.x, center_point.y)
