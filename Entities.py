"""Entities Class"""
from abc import ABC

class Entities(ABC):
    """Abstract class Entities"""
    def __init__(self, x, y):
        self.symbole = ''
        self.x_value = x
        self.y_value = y

    def get_x(self):
        """Return X attribute"""
        return self.x_value

    def get_y(self):
        """Return Y attribute"""
        return self.y_value

    def set_x(self, new_x):
        """Set X as new X attribute"""
        self.x_value = new_x

    def set_y(self, new_y):
        """Set Y as new Y attribute"""
        self.y_value = new_y

    def __str__(self):
        return self.symbole
