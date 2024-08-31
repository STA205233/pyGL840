'''
Exceptions
-

Exceptions for GL840.

----------------
Author: Shota Arai
Date: 2024/08/28
'''

from .Warning import Warning as _Warning


class GL840BaseException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(args)

    def sound(self, frequency: list[float], second: list[float], volume: float, title: str | None = None, description: str | None = None) -> None:
        title_ = title if title is not None else ""
        description_ = "\n" + description if description is not None else ""
        _Warning()(frequency, second, volume, "\n-------------" + title_ + f"-------------{description_}\nPress Ctrl+C to stop")


class ChannelNotMatchError(GL840BaseException):
    def __init__(self, description: str | None = None, title: str = "Channel Not Match Error", notify: bool = True) -> None:
        super().__init__(title, description)
        if notify:
            super().sound([880 * 2, 0, 880 * 2, 0], [0.1, 0.05, 0.1, 0.2], 0.4, title, description)


class GL840ConnectionError(GL840BaseException):
    def __init__(self, description: str | None = None, title: str = "Connection Error", notify: bool = True) -> None:
        super().__init__(title, description)
        if notify:
            super().sound([880 * 2, 0, 880 * 2, 0], [0.1, 0.05, 0.1, 0.2], 0.4, title, description)
