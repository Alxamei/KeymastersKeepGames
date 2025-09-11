from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class TinyBookshopArchipelagoOptions:
    pass


# Main Class
class TinyBookshopGame(Game):
    name = "Tiny Bookshop"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.SW
    ]

    is_adult_only_or_unrated = False

    options_cls = TinyBookshopArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="If no location is listed, sell books at LOCATION",
                data={
                    "LOCATION": (self.locations, 1),
                },
            ),
            GameObjectiveTemplate(
                label="Sell books while having a decoration tagged DECOTYPE equipped",
                data={
                    "DECOTYPE": (self.decorationtypes, 1)
                }
            )
        ]

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Sell NUMBER GENRE books",
                data={
                    "NUMBER": (self.genresellcount, 1),
                    "GENRE": (self.genres, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Sell NUMBER books at LOCATION",
                data={
                    "NUMBER": (self.booksellcount, 1),
                    "LOCATION": (self.locations, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
             GameObjectiveTemplate(
                label="Sell NUMBER books at Far Beach",
                data={
                    "NUMBER": (self.booksellcount, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Earn NUMBER coins at LOCATION",
                data={
                    "NUMBER": (self.coinscount, 1),
                    "LOCATION": (self.locations, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Earn NUMBER coins at Far Beach",
                data={
                    "NUMBER": (self.coinscount, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Buy NUMBER items at the Flea Market",
                data={
                    "NUMBER": (self.marketitems, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Attend the end of season event",
                data={},
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Recommend NUMBER GENRE books",
                data={
                    "NUMBER": (self.genrereccount, 1),
                    "GENRE": (self.genres, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Sell NUMBER books EVENT",
                data={
                    "NUMBER": (self.booksellcount, 1),
                    "EVENT": (self.events, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Sell NUMBER books in one day",
                data={
                    "NUMBER": (self.daysellcount, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Purchase NUMBER boxes of books",
                data={
                    "NUMBER": (self.bookbuycount, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Purchase NUMBER seasonal items",
                data={
                    "NUMBER": (self.seasonalbuycount, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            )
        ]
    # Datasets
    @staticmethod
    def genres() -> List[str]:
        return [
            "Crime",
            "Drama",
            "Fact",
            "Fantasy",
            "Classic",
            "Kids",
            "Travel",
        ]
    
    @staticmethod
    def locations() -> List[str]:
        return [
            "Waterfront Square",
            "Cafe Liberte",
            "Mega Marche",
            "the University",
            "the Lighthouse",
            "the Castle Ruins",
            "the Flea Market",
            "the Hospital",
            "Rye Park",
        ]
    
    @staticmethod
    def events() -> List[str]:
        return [
            "on Mega Savings Day",
            "at the Waterfront Fish Market",
            "at the Weekly Flea Market",
        ]

    @staticmethod
    def genresellcount() -> range:
        return range(1, 25)
    
    @staticmethod
    def booksellcount() -> range:
        return range(30, 200)
    
    @staticmethod
    def coinscount() -> range:
        return range(50, 1000)
    
    @staticmethod
    def marketitems() -> range:
        return range(1, 12)
    
    @staticmethod
    def genrereccount() -> range:
        return range(5, 50)
    
    @staticmethod
    def daysellcount() -> range:
        return range(30, 100)
    
    @staticmethod
    def bookbuycount() -> range:
        return range(1, 16)
    
    @staticmethod
    def seasonalbuycount() -> range:
        return range(1, 8)
    
    @staticmethod
    def decorationtypes() -> List[str]:
        return [
            "Animals",
            "Antiques",
            "Calming",
            "Classy",
            "Dangerous",
            "Distracting",
            "Electrical",
            "Festive",
            "Furniture",
            "Maritime",
            "Paintings",
            "Plants",
            "Safety Equipment",
            "Spooky",
            "Warm",
        ]
