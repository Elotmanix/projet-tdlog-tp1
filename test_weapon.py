import unittest
from Weapon import Weapon,NoAmmunitionError,OutOfRangeError,SurfaceMissile,AntiAirMissile,SubmarineTorpedo
class TestWeapon(unittest.TestCase):
    def test_fire_at_no_ammunition(self):
        weapon = Weapon(0, 100)
        with self.assertRaises(NoAmmunitionError):
            weapon.fire_at(10, 10, 10)

    def test_fire_at_out_of_range(self):
        class MockWeapon(Weapon):
            def is_valid_target(self, x, y, z):
                return False

        weapon = MockWeapon(10, 5)
        with self.assertRaises(OutOfRangeError):
            weapon.fire_at(10, 10, 10)
class TestSurfaceMissile(unittest.TestCase):
    def setUp(self):
        self.surface_missile = SurfaceMissile(10, 100)

    def test_fire_at_no_ammunition(self):
        self.surface_missile.ammunitions = 0
        with self.assertRaises(NoAmmunitionError):
            self.surface_missile.fire_at(10, 10, 0)

    def test_fire_at_out_of_range(self):
        with self.assertRaises(OutOfRangeError):
            self.surface_missile.fire_at(1000, 1000, 100)

    def test_is_valid_target_zero_z(self):
        self.assertTrue(self.surface_missile.is_valid_target(10, 10, 0))

    def test_is_valid_target_non_zero_z(self):
        self.assertFalse(self.surface_missile.is_valid_target(10, 10, 5))
class TestAntiAirMissile(unittest.TestCase):
    def setUp(self):
        self.anti_air_missile = AntiAirMissile(10, 100)

    def test_fire_at_no_ammunition(self):
        self.anti_air_missile.ammunitions = 0
        with self.assertRaises(NoAmmunitionError):
            self.anti_air_missile.fire_at(10, 10, 1)

    def test_fire_at_out_of_range(self):
        with self.assertRaises(OutOfRangeError):
            self.anti_air_missile.fire_at(1000, 1000, 100)

    def test_is_valid_target_positive_z(self):
        self.assertTrue(self.anti_air_missile.is_valid_target(10, 10, 1))

    def test_is_valid_target_zero_z(self):
        self.assertFalse(self.anti_air_missile.is_valid_target(10, 10, 0))

    def test_is_valid_target_negative_z(self):
        self.assertFalse(self.anti_air_missile.is_valid_target(10, 10, -1))
class TestSubmarineTorpedo(unittest.TestCase):
    def setUp(self):
        self.submarine_torpedo = SubmarineTorpedo(10, 100)

    def test_fire_at_no_ammunition(self):
        self.submarine_torpedo.ammunitions = 0
        with self.assertRaises(NoAmmunitionError):
            self.submarine_torpedo.fire_at(10, 10, 10)

    def test_fire_at_out_of_range(self):
        with self.assertRaises(OutOfRangeError):
            self.submarine_torpedo.fire_at(1000, 1000, 100)

    def test_is_valid_target_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.submarine_torpedo.is_valid_target(10, 10, 10)        
if __name__ == '__main__':
    unittest.main()
