from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import OptionSet, Range

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class HadesIIArchipelagoOptions:
	hades_ii_content_types_allowed: HadesIIContentTypesAllowed
	hades_ii_aspect_selection: HadesIIAspectSelection
	hades_ii_weapon_selection: HadesIIWeaponSelection
	hades_ii_fear_lower_bound: HadesIIFearLowerBound
	hades_ii_fear_upper_bound: HadesIIFearUpperBound

class HadesIIGame(Game):

	name = "Hades II"
	platform = KeymastersKeepGamePlatforms.PC

	platforms_other = [
		KeymastersKeepGamePlatforms.SW,
		KeymastersKeepGamePlatforms.SW2,
	]

	is_adult_only_or_unrated = False

	options_cls = HadesIIArchipelagoOptions

	# Optional Game Constraints
	def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
		return [
			GameObjectiveTemplate(
				label="Keepsake: KEEPSAKE Familiar: FAMILIAR Use Arcana: ARCANA",
				data={
					"KEEPSAKE": (self.KEEPSAKE,1),
					"FAMILIAR": (self.FAMILIAR,1),
					"ARCANA": (self.ARCANA,1),
				},
			),
		]

	#Main Objectives
	def game_objective_templates(self) -> List[GameObjectiveTemplate]:

		objective_list = list()

		if "Weapon Aspects" in self.content_types_allowed():
			objective_list += [
				GameObjectiveTemplate(
					label="Beat a LOCATION run with the ASPECT",
					data={
						"LOCATION": (self.LOCATION,1),
						"ASPECT": (lambda: self.allowed_aspects(),1),
					},
					is_time_consuming=True,
					is_difficult=False,
					weight=5,
				),
				GameObjectiveTemplate(
					label="Defeat BOSS with the ASPECT",
					data={
						"BOSS": (self.BOSS,1),
						"ASPECT": (lambda: self.allowed_aspects(),1),
					},
					is_time_consuming=False,
					is_difficult=False,
					weight=15,
				),
			]
		else:
			objective_list += [
				GameObjectiveTemplate(
					label="Beat a LOCATION run with the WEAPON",
					data={
						"LOCATION": (self.LOCATION,1),
						"WEAPON": (lambda: self.allowed_weapons(),1),
					},
					is_time_consuming=True,
					is_difficult=False,
					weight=5,
				),
				GameObjectiveTemplate(
					label="Defeat BOSS with the WEAPON",
					data={
						"BOSS": (self.BOSS,1),
						"WEAPON": (lambda: self.allowed_weapons(),1),
					},
					is_time_consuming=False,
					is_difficult=True,
					weight=15,
				),
			]
		
		if "Vows" in self.content_types_allowed():
			objective_list += [
				GameObjectiveTemplate(
					label="Beat a LOCATION run with minimum FEAR fear including at least one rank of Vow of VOW",
					data={
						"LOCATION": (self.LOCATION, 1),
						"FEAR": (lambda: self.fear_range(),1),
						"VOW": (self.VOW,1),
					},
					is_time_consuming=True,
					is_difficult=False,
					weight=5,
				),
				GameObjectiveTemplate(
					label="Defeat BOSS with minimum FEAR fear including at least one rank of Vow of VOW",
					data={
						"BOSS": (self.BOSS, 1),
						"FEAR": (lambda: self.fear_range(),1),
						"VOW":	(self.VOW,1),
					},
					is_time_consuming=False,
					is_difficult=False,
					weight=15,
				),
			]
		if "Chaos Below and Above" in self.content_types_allowed():
			objective_list += [
				GameObjectiveTemplate(
					label="Complete a run of CHAOSAB",
					data={
						"CHAOSAB": (self.CHAOSAB,1),
					},
					is_time_consuming=True,
					is_difficult=False,
					weight=1,
				),
			]
		if "Chaos Trials" in self.content_types_allowed():
			if "Moonstone Axe" in self.allowed_weapons() or "Moonstone Axe - Aspect of Melinoe" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the TRIAL",
						data={
							"TRIAL": (self.MATRIAL,1),
						},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Argent Skull" in self.allowed_weapons() or "Argent Skull - Aspect of Melinoe" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the TRIAL",
						data={
							"TRIAL": (self.ASTRIAL,1),
						},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Umbral Flames" in self.allowed_weapons() or "Umbral Flames - Aspect of Melinoe" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the TRIAL",
						data={
							"TRIAL": (self.UFTRIAL,1),
						},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Witch's Staff" in self.allowed_weapons() or "Witch's Staff - Aspect of Melinoe" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of Origin",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
					GameObjectiveTemplate(
						label="Complete the Trial of Humility",
						data={},
						is_time_consuming=False,
						is_difficult=True,
						weight=5,
					),
				]
			if "Sister Blades" in self.allowed_weapons() or "Sister Blades - Aspect of Melinoe" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of Salt",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
					GameObjectiveTemplate(
						label="Complete the Trial of Destiny",
						data={},
						is_time_consuming=False,
						is_difficult=True,
						weight=5,
					),
				]
			if "Black Coat" in self.allowed_weapons() or "Black Coat - Aspect of Melinoe" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of Glory",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
					GameObjectiveTemplate(
						label="Complete the Trial of Haste",
						data={},
						is_time_consuming=False,
						is_difficult=True,
						weight=5,
					),
				]
		if "Chaos Trials" in self.content_types_allowed() and "Weapon Aspects" in self.content_types_allowed():
			if "Argent Skull - Aspect of Persephone" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of the Fall",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Moonstone Axe - Aspect of Charon" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of the Moon",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Witch's Staff - Aspect of Momus" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of Vigor",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Umbral Flames - Aspect of Moros" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of Flame",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Sister Blades - Aspect of Pan" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of Gold",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Black Coat - Aspect of Selene" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of Fury",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Argent Skull - Aspect of Medea" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of Precarity",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Umbral Flames - Aspect of Eos" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of Heartache",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Moonstone Axe - Aspect of Nergal" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of the Marauder",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Argent Skull - Aspect of Hel" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of the Outcast",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Witch's Staff - Aspect of Anubis" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of the Jackal",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Sister Blades - Aspect of the Morrigan" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of the Banshee",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Umbral Flames - Aspect of Supay" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of the Daemon",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Black Coat - Aspect of Shiva" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of the Supreme",
						data={},
						is_time_consuming=False,
						is_difficult=False,
						weight=5,
					),
				]
			if "Sister Blades - Aspect of Artemis" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of Blood",
						data={},
						is_time_consuming=False,
						is_difficult=True,
						weight=5,
					),
				]
			if "Witch's Staff - Aspect of Circe" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of the Drifter",
						data={},
						is_time_consuming=False,
						is_difficult=True,
						weight=5,
					),
				]
			if "Black Coat - Aspect of Nyx" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of the Fairest",
						data={},
						is_time_consuming=False,
						is_difficult=True,
						weight=5,
					),
				]
			if "Moonstone Axe - Aspect of Thanatos" in self.allowed_aspects():
				objective_list += [
					GameObjectiveTemplate(
						label="Complete the Trial of Doom",
						data={},
						is_time_consuming=False,
						is_difficult=True,
						weight=5,
					),
				]
		objective_list += [
			GameObjectiveTemplate(
				label="Defeat BOSS with a boon from GOD",
				data={
					"BOSS": (self.BOSS,1),
					"GOD": (self.GOD,1),
				},
				is_time_consuming=False,
				is_difficult=False,
				weight=10,
			),
			GameObjectiveTemplate(
				label="Defeat BOSS with a boon from Hermes",
				data={
					"BOSS": (self.BOSS,1),
				},
				is_time_consuming=True,
				is_difficult=False,
				weight=4,
			),
			GameObjectiveTemplate(
				label="Defeat BOSS with a boon from Athena",
				data={
					"BOSS": (self.BOSS,1),
				},
				is_time_consuming=False,
				is_difficult=True,
				weight=3,
			),
			GameObjectiveTemplate(
				label="Defeat BOSS with a boon from Artemis",
				data={
					"BOSS": (self.BOSS,1),
				},
				is_time_consuming=True,
				is_difficult=True,
				weight=1,
			),
		]

		return objective_list


	def content_types_allowed(self) -> List[str]:
		value = self.archipelago_options.hades_ii_content_types_allowed.value
		return list(value) if value is not None else []
	
	def allowed_aspects(self) -> List[str]:
		value = self.archipelago_options.hades_ii_aspect_selection.value
		return list(value) if value is not None else []
	
	def allowed_weapons(self) -> List[str]:
		value = self.archipelago_options.hades_ii_weapon_selection.value
		return list(value) if value is not None else []
	
	@property
	def fear_bounds(self) -> tuple:
		lower_fear = int(self.archipelago_options.hades_ii_fear_lower_bound.value)
		upper_fear = int(self.archipelago_options.hades_ii_fear_upper_bound.value)
		return (lower_fear, upper_fear)

	def fear_range(self) -> List[int]:
		bounds = self.fear_bounds
		min_fear = max(0, bounds[0])
		max_fear = min(32, bounds[1])
		return list(range(min_fear, max_fear + 1))


	@staticmethod
	def FAMILIAR() -> List[str]:
		return [
			"Frinos",
			"Raki",
			"Toula",
			"Hecuba",
			"Gale",
		]

	@staticmethod
	def BOSS() -> List[str]:
		return [
			"Hecate",
			"Scylla and the Sirens",
			"Cerberus",
			"Polyphemus",
			"Eris",
			"Prometheus",
		]

	@staticmethod
	def LOCATION() -> List[str]:
		return [
			"Surface",
			"Underworld",
		]

	@staticmethod
	#All gods here are forceable by their keepsakes with no additional requirement
	def GOD() -> List[str]:
		return [
			"Zeus",
			"Hera",
			"Poseidon",
			"Demeter",
			"Apollo",
			"Aphrodite",
			"Hephaestus",
			"Hestia",
			"Ares",
			"Selene",
		]

	@staticmethod
	def KEEPSAKE() -> List[str]:
		return [
			"Silver Wheel",
			"Knuckle Bones",
			"Luckier Tooth",
			"Ghost Onion",
			"Evil Eye",
			"Gold Purse",
			"Engraved Pin",
			"Discordant Bell",
			"Mettalic Droplet",
			"White Antler",
			"Moon Beam",
			"Cloud Bangle",
			"Iridescent Fan",
			"Vivid Sea",
			"Barley Sheaf",
			"Harmonic Photon",
			"Beautiful Mirror",
			"Adamant Shard",
			"Everlasting Ember",
			"Sword Hilt",
			"Gorgon Amulet",
			"Fig Leaf",
			"Silken Sash",
			"Aromatic Phial",
			"Concave Stone",
			"Lion Fang",
			"Blackened Fleece",
			"Crystal Figurine",
			"Experimental Hammer",
			"Jeweled Pom",
			"Calling Card",
			"Time Piece",
			"Transcendent Embryo",
		]

	@staticmethod

	def ARCANA() -> List[str]:
		return [
			"The Sorceress (I)",
			"The Wayward Son (II)",
			"The Huntress (III)",
			"Eternity (IV)",
			"The Moon (V)",
			"The Furies (VI)",
			"Persistence (VII)",
			"The Messenger (VIII)",
			"The Unseen (IX)",
			"Night (X)",
			"The Swift Runner (XI)",
			"Death (XII)",
			"The Centaur (XIII)",
			"Origination (XIV)",
			"The Lovers (XV)",
			"The Enchantress (XVI)",
			"The Boatman (XVII)",
			"The Artificer (XVIII)",
			"Excellence (XIX)",
			"The Queen (XX)",
			"The Fates (XXI)",
			"The Champions (XXII)",
			"Strength (XXIII)",
			"Divinity (XXIV)",
			"Judgement (XXV)",
		]

	@staticmethod

	def VOW() -> List[str]:
		return [
			"Pain",
			"Grit",
			"Wards",
			"Frenzy",
			"Hordes",
			"Menace",
			"Return",
			"Fangs",
			"Scars",
			"Debt",
			"Shadow",
			"Forfeit",
			"Time",
			"Void",
			"Hubris",
			"Denial",
			"Rivals",
		]

	@staticmethod

	def CHAOSAB() -> List[str]:
		return [
			"Chaos Above",
			"Chaos Below",
		]

	@staticmethod
	#Moonstone Axe Melinoe Aspect Trials
	def MATRIAL() -> List[str]:
		return [
			"Trial of Brawn",
			"Trial of Slaughter",
		]

	@staticmethod
	#Argent Skull Melinoe Aspect Trials
	def ASTRIAL() -> List[str]:
		return [
			"Trial of Vengeance",
			"Trial of the Flock",
		]

	@staticmethod
	#Umbral Flames Melinoe Aspect Trials
	def UFTRIAL() -> List[str]:
		return [
			"Trial of Thunder",
			"Trial of the Maiden",
		]

class HadesIIContentTypesAllowed(OptionSet):

	"""
	Indicates what types of optional content the player would like to include.

	Note: Opting in to Chaos Below and Above will include highly rng checks that may be extra difficult to achieve due to their random nature. It requires time consuming to be marked as "on" as well as being included here to be included in the challenge pool.
	"""


	display_name = "Hades II Allowed Content Types"
	valid_content = [
   		"Vows",
		"Weapon Aspects",
		"Chaos Trials",
   		"Chaos Below and Above",
	]

	default = valid_content


class HadesIIAspectSelection(OptionSet):

	"""
	Choose what aspects can be rolled for challenges if “Weapon Aspects” is in the allowed content types.

	It is recommended to remove any aspects you have not unlocked or are not comfortable with clearing a run on.

	"""


	display_name = "Hades II Aspect Selection"
	valid_aspects = [
    	# Witch’s Staff
  		"Witch's Staff - Aspect of Melinoe",
		"Witch's Staff - Aspect of Circe",
		"Witch's Staff - Aspect of Momus",
   		"Witch's Staff - Aspect of Anubis",
   		# Sister Blades
   		"Sister Blades - Aspect of Melinoe",
		"Sister Blades - Aspect of Artemis",
		"Sister Blades - Aspect of Pan",
		"Sister Blades - Aspect of the Morrigan",
		# Umbral Flames
   		"Umbral Flames - Aspect of Melinoe",
		"Umbral Flames - Aspect of Moros",
		"Umbral Flames - Aspect of Eos",
		"Umbral Flames - Aspect of Supay",
    	# Moonstone Axe
   		"Moonstone Axe - Aspect of Melinoe",
		"Moonstone Axe - Aspect of Charon",
   		"Moonstone Axe - Aspect of Thanatos",
		"Moonstone Axe - Aspect of Nergal",
    	# Argent Skull
  		"Argent Skull - Aspect of Melinoe",
		"Argent Skull - Aspect of Medea",
		"Argent Skull - Aspect of Persephone",
		"Argent Skull - Aspect of Hel",
    	#Black Coat
   		"Black Coat - Aspect of Melinoe",
  		"Black Coat - Aspect of Selene",
		"Black Coat - Aspect of Nyx",
		"Black Coat - Aspect of Shiva",
	]

	default = valid_aspects

class HadesIIWeaponSelection(OptionSet):

	"""
	Choose what weapons can be rolled for challenges if “Weapon Aspects” is NOT in the allowed content types.
	
	It is recommended to remove any weapons you have not unlocked or are not comfortable with clearing a run on.

	"""

	display_name = "Hades II Weapon Selection"
	valid_weapons = [
		"Witch's Staff",
		"Sister Blades",
		"Umbral Flames",
		"Moonstone Axe",
		"Argent Skull",
		"Black Coat",
	]

	default = valid_weapons

class HadesIIFearLowerBound(Range):
	"""
	Minimum number of Fear required for checks if "Vows" are a selected content type.

	Maximum Allowed Fear is 32 for this implementation
	"""

	display_name = "Hades II Fear Minimum"
	default = 4
	range_start = 0
	range_end = 32

class HadesIIFearUpperBound(Range):
	"""
	Maximum number of Fear required for checks if "Vows" are a selected content type.
	
	Maximum Allowed Fear is 32 for this implementation
	"""

	display_name = "Hades II Fear Maximum"
	default = 12
	range_start = 0
	range_end = 32