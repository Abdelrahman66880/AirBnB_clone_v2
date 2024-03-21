#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
import uuid


class Place(BaseModel):
    """ A place to stay """
    def __init__(self, *args, **kwargs):
        """Initialization method for Place"""
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4())  # Initialize id attribute

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
