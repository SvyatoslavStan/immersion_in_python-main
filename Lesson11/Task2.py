class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        return None

    def __str__(self):
        return "Вода"


class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Water):
            return Storm()
        return None

    def __str__(self):
        return "Воздух"


class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        return None

    def __str__(self):
        return "Огонь"


class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        return None

    def __str__(self):
        return "Земля"


class Storm:
    def __str__(self):
        return "Шторм"


class Steam:
    def __str__(self):
        return "Пар"


class Mud:
    def __str__(self):
        return "Грязь"


class Lightning:
    def __str__(self):
        return "Молния"


class Dust:
    def __str__(self):
        return "Пыль"


class Lava:
    def __str__(self):
        return "Лава"


class Cold:
    def __add__(self, other):
        if isinstance(other, Water):
            return Ice()
        elif isinstance(other, Fire):
            return Smoke()
        return None

    def __str__(self):
        return "Холод"


class Ice:
    def __str__(self):
        return "Лёд"


class Smoke:
    def __str__(self):
        return "Дым"


water = Water()
air = Air()
fire = Fire()
earth = Earth()
cold = Cold()

print(water + air)  
print(water + fire)  
print(water + earth)  
print(air + fire)  
print(air + earth) 
print(fire + earth)  
print(water + cold)  
print(fire + cold)  
print(air + cold)  
