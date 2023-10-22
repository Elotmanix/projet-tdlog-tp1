# Exceptions
class NoAmmunitionError(Exception):
    pass

class OutOfRangeError(Exception):
    pass

# Superclasse Weapon
class Weapon:
    def __init__(self, ammunitions, range):
        self.ammunitions = ammunitions
        self.range = range

    def fire_at(self, x, y, z):
        if self.ammunitions == 0:
            raise NoAmmunitionError("No ammunition left.")
        if not self.is_valid_target(x, y, z):
            self.ammunitions -= 1
            raise OutOfRangeError("Target out of range.")

    def is_valid_target(self, x, y, z):
        raise NotImplementedError("Must be implemented by subclass.")

# Sous-classes
class SurfaceMissile(Weapon):
    def __init__(self, ammunitions, range):
        super().__init__(ammunitions, range)

    def is_valid_target(self, x, y, z):
        return z == 0

class AntiAirMissile(Weapon):
    def __init__(self, ammunitions, range):
        super().__init__(ammunitions, range)

    def is_valid_target(self, x, y, z):
        return z > 0

class SubmarineTorpedo(Weapon):
    def __init__(self, ammunitions, range):
        super().__init__(ammunitions, range)

    def is_valid_target(self, x, y, z):
        return z <= 0
