from enum import Enum

class Color():
    DEFAULT = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"

class Direction():
    NORTH = (0, 1)
    EAST = (1, 0)
    SOUTH = (0, -1)
    WEST = (-1, 0)

    def multiply_tuple(tuple1: tuple[int], tuple2: tuple[int]) -> tuple:
        return (tuple1[0] * tuple2[0], tuple1[1] * tuple2[1])

    @classmethod
    def opposite(cls, direction: tuple[int]) -> tuple[int]:
        return cls.multiply_tuple(direction, (-1, -1))

    def char_to_vector(char: str) -> tuple[int]:
        if char == "^":
            return Direction.NORTH
        elif char == ">":
            return Direction.EAST
        elif char == "v":
            return Direction.SOUTH
        elif char == "<":
            return Direction.WEST
        else:
            raise ValueError(f"{char} is not a valid direction character")
    
    def vector_to_char(vector: tuple[int]):
        if vector == Direction.NORTH:
            return "^"
        elif vector == Direction.EAST:
            return ">"
        elif vector == Direction.SOUTH:
            return "v"
        elif vector == Direction.WEST:
            return "<"
        else:
            raise ValueError(f"{vector} is not a valid direction vector")


    def next_clockwise_cardinal(direction: tuple[int]) -> tuple[int]:
        x = direction[0]
        y = direction[1]
        return (y, x * -1)

    
if __name__ == "__main__":
    print(Direction.next_clockwise_cardinal(Direction.NORTH))
    print(Direction.next_clockwise_cardinal(Direction.EAST))
    print(Direction.next_clockwise_cardinal(Direction.SOUTH))
    print(Direction.next_clockwise_cardinal(Direction.WEST))
    print(Direction.char_to_vector("^"))