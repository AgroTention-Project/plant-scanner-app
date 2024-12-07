"""Sacnner application
"""

from .scanner.potato import potato_scanner
from .scanner.rice import rice_scanner
from .scanner.tomato import tomato_scanner


__all__ = [
    "potato_scanner",
    "rice_scanner",
    "tomato_scanner",
]
