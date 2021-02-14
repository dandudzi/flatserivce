#!/usr/bin/env python

__author__ = "Daniel Dudziak"
__license__ = "GNU GPL 3.0"
__version__ = "1.0.0"

import sys


class HTTPDomainSpecification:
    def __init__(self, url: str, subdomain: str, file_extension: str):
        self.file_extension = file_extension
        self.subdomain = subdomain
        self.url = url


class Range:
    def __init__(self, min: int = 0, max: int = sys.maxsize):
        self.max = max
        self.min = min


class SurfaceRange(Range):
    pass


class NumberOfRooms(Range):
    pass


class FlatProperty:
    def __init__(self, domain: HTTPDomainSpecification, surface: SurfaceRange, rooms: NumberOfRooms):
        self.surface = surface
        self.rooms = rooms
        self.domain = domain
