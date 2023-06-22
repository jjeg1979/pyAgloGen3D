from dataclasses import dataclass

from src.coordinates.coordinates import Coordinates


@dataclass
class Particle:
    """Represents an spherical particle"""

    id: int
    coordinates: Coordinates
