#!/usr/bin/env python

__author__ = "Daniel Dudziak"
__license__ = "GNU GPL 3.0"
__version__ = "1.0.0"
import logging

from com.daniel.dudziak.flatservice.flat.dto.Flat import Flat


class FlatReader:
    def set_flat_property(self, flat_property):
        self.flat_property = flat_property

    def read(self) -> [Flat]:
        logging.error("FlatReader not found")
        exit(1)