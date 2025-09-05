from abc import ABC, abstractmethod


class Attack(ABC):
    """
    An attack
    """

    # -------------------------------------------------------------------------
    # Constructor
    # -------------------------------------------------------------------------

    def __init__(self, _power: int, _name: str, _description: str):
        self._power: int = _power
        self._name: str = _name
        self._description: str = _description

    @abstractmethod
    def compute_damage(APkm) -> int:
        None

    # -------------------------------------------------------------------------
    # Getters and Setters
    # -------------------------------------------------------------------------

    @property
    def power(self):
        return self._power

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description
