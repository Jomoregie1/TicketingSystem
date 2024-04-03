from theatre import Theatre
from abc import ABC, abstractmethod


class BaseUser(ABC):
    _theatre = None

    @classmethod
    def get_theatre(cls):
        if cls._theatre is None:
            cls._theatre = Theatre()
        return cls._theatre

    @abstractmethod
    def cancel_ticket(self):
        pass

    @abstractmethod
    def display_menu(self):
        pass


