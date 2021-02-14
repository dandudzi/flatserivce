#!/usr/bin/env python

__author__ = "Daniel Dudziak"
__license__ = "GNU GPL 3.0"
__version__ = "1.0.0"

from com.daniel.dudziak.flatservice.flat import FlatServiceAPI

import logging
import sys
import re


def init():
    properties_file_path = "sites_settings.json"
    level_logging = logging.INFO
    logging_file_name = 'flat.log'
    for arg in sys.argv[1:]:
        if arg == "Debug":
            level_logging = logging.DEBUG
        elif re.search("^.*\.json", arg) is not None:
            properties_file_path = arg

    logging.basicConfig(level=level_logging,
                        format='%(asctime)s [%(threadName)s] [%(levelname)s] %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        handlers=[
                            logging.FileHandler(logging_file_name),
                            logging.StreamHandler()
                        ]
                        )
    logging.info("Level logging: %s", logging.getLevelName(level_logging))
    logging.info("Logging file name: %s", logging_file_name)
    logging.info("File property: %s", properties_file_path)

    return FlatServiceAPI.FlatServiceApi(properties_file_path)
