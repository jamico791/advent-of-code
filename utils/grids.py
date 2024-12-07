if __name__ == "__main__":
    from globals import Color, Direction

else:
    from utils.globals import Color, Direction

class Point:
    def __init__(self, x: int, y: int, color: str = Color.GREEN):
        self.x = x
        self.y = y
        self.color = color
    
    def __repr__(self):
        return f"{self.color}x={self.x}, y={self.y}{Color.DEFAULT}"
    
    def move(self, x: int, y: int):
        self.x = x
        self.y = y

    def shift(self, vector: list[int]):
        self.x += vector[0]
        self.y -= vector[1]
    
    def shift_direction_char(self, char: str):
        if char == "^":
            self.shift(Direction.NORTH)
        elif char == "v":
            self.shift(Direction.SOUTH)
        elif char == ">":
            self.shift(Direction.EAST)
        elif char == "<":
            self.shift(Direction.WEST)

class Grid:
    """A work in progress class to solve grid related problems"""
    def __init__(self, rows: int = 0, cols: int = 0, default: any = None, lines: list[str|list] = None, infinite: bool = False):
        if rows > 0 and cols > 0:
            self.data = [[default if default != None else y + 1 for y in range(cols)] for x in range(rows)]
            self.height = rows
            self.width = cols
        elif lines:
            self.data = [[str(unit) for unit in line] for line in lines]
            self.height = len(self.data)
            self.width = len(self.data[0])
        else:
            raise ValueError("You have to specify either rows and cols, or lines")
        self.default = default
        self.infinite = infinite
        self.points: set[Point] = set()

    def __repr__(self):
        self.update_size()
        res = ""
        i = 0
        for row in self.data:
            j = 0
            for char in row:
                point = None
                for p in self.points:
                    if p.x == j and p.y == i:
                        point = p
                if j > 0:
                    res += " "
                if point:
                    res += point.color
                res += str(char)
                if point:
                    res += Color.DEFAULT
                if i < len(self.data) - 1 and j == len(row) - 1:
                    res += "\n"
                j += 1
            i += 1
        return res

    def add_point(self, point: Point):
        self.points.add(point)

    def get_value(self, point: Point):
        self.update_size()
        return self.data[point.y][point.x]

    def set_value(self, point: Point, new_value: any):
        self.update_size()
        self.data[point.y][point.x] = new_value

    def get_relative_value(self, point: Point, vector: list[int]):
        self.update_size()
        relative_x = point.x + vector[0]
        relative_y = point.y - vector[1]
        if relative_x < 0 or relative_x >= self.width or relative_y < 0 or relative_y >= self.height:
            return None
        return self.data[relative_y][relative_x]

    def increment(self, point: Point):
        self.update_size()
        self.data[point.y][point.x] += 1

    def decrement(self, point: Point):
        self.update_size()
        self.data[point.y][point.x] -= 1

    def update_size(self):
        for point in self.points:
            if self.infinite:
                if point.x < 0:
                    for other_point in self.points:
                        if point != other_point:
                            other_point.shift([-1, 0])
                    for row in self.data:
                        for _ in range(0 - point.x):
                            row.insert(0, self.default)
                    point.x = 0
                    self.width = len(self.data[0])
                elif point.x > self.width - 1:
                    for row in self.data:
                        for _ in range(point.x - (self.width - 1)):
                            row.append(self.default)
                    self.width = len(self.data[0])
                if point.y < 0:
                    for other_point in self.points:
                        if point != other_point:
                            other_point.shift([0, 1])
                    for _ in range(0 - point.y):
                        self.data.insert(0, [self.default for n in range(self.width)])
                    point.y = 0
                    self.height = len(self.data)
                if point.y > self.height - 1:
                    for _ in range(point.y - (self.height - 1)):
                        self.data.append([self.default for n in range(self.width)])
                    self.height = len(self.data)
            else:
                if point.x < 0 or point.y < 0 or point.x > self.width - 1 or point.y > self.height - 1:
                    raise ValueError("The pointer must lie within the boundaries of the grid.")

if __name__ == "__main__":
    point = Point(0, 0, color=Color.BLUE)
    grid = Grid(rows=2, cols=2, default=0, infinite=True)
    grid.add_point(point)
    grid.set_value(point, 3)
    print(grid)
    print()
    # print(grid)
    point.shift([0, 1])
    print(grid)
    print(grid.get_relative_value(point, [0, 1]))