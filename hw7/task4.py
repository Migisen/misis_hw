class Water:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        else:
            return None


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Earth:
    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        elif isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        else:
            return None


class Dirt:
    ...


class Storm:
    ...


class Steam:
    ...


class Lightning:
    ...


class Dust:
    ...


class Lava:
    ...


if __name__ == "__main__":
    result = Fire() + Air()
    print(result)
