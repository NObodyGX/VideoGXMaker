
from typing import Any


class Singleton(object):
    __instance = None

    def __new__(cls) -> Any:
        if not Singleton.__instance:
            Singleton.__instance = object.__new__(cls)
        return Singleton.__instance