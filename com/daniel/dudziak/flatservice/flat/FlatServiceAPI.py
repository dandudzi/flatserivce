#!/usr/bin/env python

__author__ = "Daniel Dudziak"
__license__ = "GNU GPL 3.0"
__version__ = "1.0.0"

import logging

from com.daniel.dudziak.flatservice.flat.services import FlatPropertyFileReader


class FlatServiceApi:
    def __init__(self, properties_file_path):
        flat_property_reader = FlatPropertyFileReader.FlatPropertyFileReader(properties_file_path)
        self.flat_properties = flat_property_reader.get_flat_properties()

    def update_flats(self):
        logging.debug("Starting to update flats")
        pass

    def print_new_flats(self):
        logging.debug("Starting to print new flats")
        pass

    def print_all_flats(self):
        logging.debug("Starting to print all flats")
        pass
