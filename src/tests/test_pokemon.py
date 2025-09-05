"""from business_object.pokemon.abstract_pokemon import Pokemon
from business_object.statistic import Statistic


class TestPokemon:
    def test_level_up(self):
        # GIVEN
        snorlax = Pokemon(stat_current=Statistic(sp_atk=100, sp_def=100))

        # WHEN
        snorlax.level_up()

        # THEN
        assert snorlax.level == 1


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
"""