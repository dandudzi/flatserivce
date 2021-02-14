#!/usr/bin/env python

__author__ = "Daniel Dudziak"
__license__ = "GNU GPL 3.0"
__version__ = "1.0.0"

import logging
import json

from com.daniel.dudziak.flatservice.flat.dto.FlatProperty import HTTPDomainSpecification, SurfaceRange, NumberOfRooms, \
    FlatProperty, Localizations, Level, BuiltYear


class FlatPropertyFileReader:
    def __init__(self, properties_file_path):
        logging.debug("Starting to load flat properties")
        self.properties = properties_file_path
        logging.debug("Flat properties loaded")

    def get_flat_properties(self) -> []:
        with open(self.properties) as json_file:
            data = json.load(json_file)
            for flat in data['flats']:
                domain_spec = HTTPDomainSpecification.from_json(flat['site'])
                surface = SurfaceRange.from_json(flat['surfaceRange'])
                rooms = NumberOfRooms.from_json(flat['numberOfRooms'])
                localizations = Localizations(flat['localizations'])
                level = Level.from_json(flat['level'])
                built_year = BuiltYear.from_json(flat['builtYear'])
                logging.info(FlatProperty(domain_spec, surface, rooms, localizations, level, built_year))
        pass
