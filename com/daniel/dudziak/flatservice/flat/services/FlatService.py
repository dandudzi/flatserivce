#!/usr/bin/env python

__author__ = "Daniel Dudziak"
__license__ = "GNU GPL 3.0"
__version__ = "1.0.0"

import logging
from com.daniel.dudziak.flatservice.flat.dto.Flat import Flat
from com.daniel.dudziak.flatservice.flat.services.FlatReader import FlatReader
from com.daniel.dudziak.flatservice.flat.dto.FlatProperty import FlatProperty
from com.daniel.dudziak.flatservice.flat.services.TrojmiastoFlatReader import TrojmiastoFlatReader



class FlatService:
    readers = {
        'trojmiasto': TrojmiastoFlatReader()
    }

    def get_flats(self, flat_readers: [FlatReader]) -> [Flat]:
        flats = []
        for flat_reader in flat_readers:
            flats += flat_reader.read()
        return flats

    def get_readers(self, flat_properties: [FlatProperty]) -> [FlatReader]:
        flat_readers = []
        for flat_property in flat_properties:
            flat_reader = FlatService.readers.get(flat_property.domain.name)
            flat_reader.set_flat_property(flat_property)
            flat_readers += [flat_reader]
        return flat_readers

