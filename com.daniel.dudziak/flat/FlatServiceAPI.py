#!/usr/bin/env python

__author__ = "Daniel Dudziak"
__license__ = "GNU GPL 3.0"
__version__ = "1.0.0"

import logging


class FlatServiceApi:
    def __init__(self, properties_file_path):
        logging.debug("Starting to load flat properties")
        self.properties = properties_file_path
        logging.debug("Flat properties loaded")

    def update_flats(self):
        logging.debug("Starting to update flats")

    def print_new_flats(self):
        logging.debug("Starting to print new flats")

    def print_all_flats(self):
        logging.debug("Starting to print all flats")
