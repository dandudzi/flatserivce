#!/usr/bin/env python

__author__ = "Daniel Dudziak"
__license__ = "GNU GPL 3.0"
__version__ = "1.0.0"

import logging


class FlatPropertyFileReader:
    def __init__(self, properties_file_path):
        logging.debug("Starting to load flat properties")
        self.properties = properties_file_path
        logging.debug("Flat properties loaded")

    @classmethod
    def get_flat_properties(cls):
        pass
