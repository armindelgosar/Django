from typing import Any


class BaseAdvertising:
    clicks = 0
    views = 0

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def incViews(self):
        self.views += 1

    def incClicks(self):
        self.clicks += 1

    @staticmethod
    def describeMe():
        print("nothing!")
