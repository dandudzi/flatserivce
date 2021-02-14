#!/usr/bin/env python

__author__ = "Daniel Dudziak"
__license__ = "GNU GPL 3.0"
__version__ = "1.0.0"

from Inital import init

if __name__ == "__main__":
    flatService = init()
    flatService.update_flats()
    flatService.print_new_flats()
