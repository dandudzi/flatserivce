#!/usr/bin/env python

__author__ = "Daniel Dudziak"
__license__ = "GNU GPL 3.0"
__version__ = "1.0.0"

import sys


class Scheme:
    def __init__(self, localization: str, surface: str, rooms: str, level: str, year: str):
        self.year = year
        self.level = level
        self.rooms = rooms
        self.surface = surface
        self.localization = localization

    def __repr__(self) -> str:
        return "[" + type(self).__name__ + ":year='" + str(self.year) + "', level='" + str(
            self.level) + "', rooms='" + str(
            self.rooms) + "', surface='" + str(self.surface) + "', localization='" + str(
            self.localization) + "']"

    @staticmethod
    def from_json(json_obj):
        localization = json_obj['localizationSchema']
        surface = json_obj['surfaceScheme']
        rooms = json_obj['roomsScheme']
        level = json_obj['levelScheme']
        year = json_obj['builtYearScheme']
        return Scheme(localization, surface, rooms, level, year)


class HTTPDomainSpecification:
    def __init__(self, url: str, subdomain: str, file_extension: str, name: str, scheme):
        self.scheme = scheme
        self.file_extension = file_extension
        self.subdomain = subdomain
        self.url = url
        self.name = name

    def __repr__(self) -> str:
        return "[" + type(self).__name__ + ":name='" + str(self.name) + "',url='" + str(
            self.url) + "', subdomain='" + str(
            self.subdomain) + "', file_extension='" + str(self.file_extension) + "',\nscheme='" + str(
            self.scheme) + "'\n]"

    @staticmethod
    def from_json(json_obj):
        name = json_obj['name']
        url = json_obj['url']
        subdomain = json_obj['subdomain']
        file_extension = json_obj['fileExtension']
        scheme = Scheme.from_json(json_obj['schemes'])
        return HTTPDomainSpecification(url, subdomain, file_extension, name, scheme)


class Range:
    def __init__(self, min: int = 0, max: int = sys.maxsize):
        self.max = max
        self.min = min

    def __repr__(self) -> str:
        return "[" + type(self).__name__ + ": min='" + str(self.min) + "' , max='" + str(self.max) + "']"

    @staticmethod
    def from_json(json_obj):
        min = json_obj['min']
        if 'max' in json_obj:
            max = json_obj['max']
            return Range(min, max)
        return Range(min, None)


class SurfaceRange(Range):
    pass


class NumberOfRooms(Range):
    pass


class BuiltYear(Range):
    pass


class Level(Range):
    pass


class Localizations:
    def __init__(self, localizations):
        self.localizations = localizations

    def __repr__(self) -> str:
        return "[" + type(self).__name__ + ": localizations='" + str(self.localizations) + "']"


class FlatProperty:
    def __init__(self, domain: HTTPDomainSpecification, surface: SurfaceRange, rooms: NumberOfRooms,
                 localizations: Localizations, level: Level, built_year: BuiltYear):
        self.built_year = built_year
        self.level = level
        self.localizations = localizations
        self.surface = surface
        self.rooms = rooms
        self.domain = domain

    def __repr__(self) -> str:
        return "[" + type(self).__name__ + ":\ndomain='" + str(self.domain) + "',\nrooms='" + str(
            self.rooms) + "',\nsurface='" + str(
            self.surface) + "',\nbuilt_year='" + str(
            self.built_year) + "',\nlevel='" + str(
            self.level) + "',\nlocalizations='" + str(
            self.localizations) + "'\n]"
