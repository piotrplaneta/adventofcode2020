import math
import numpy

class Tile():
    def __init__(self, id, content):
        self.id, self.content = id, content
        self.neighbours = [None, None, None, None]

    def __key(self):
        return (self.id)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __repr__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)

    def borders(self):
        return [
            self.top_border(),
            self.right_border(),
            self.bottom_border(),
            self.left_border()
        ]

    def inner_content(self):
        inner = []
        for i in range(1,9):
            inner.append(self.content[i][1:9])

        return inner

    def possible_borders(self):
        return self.borders() + [border[::-1] for border in self.borders()]

    def top_border(self):
        return self.content[0]

    def bottom_border(self):
        return self.content[9]

    def left_border(self):
        return "".join([self.content[i][0] for i in range(10)])

    def right_border(self):
        return "".join([self.content[i][9] for i in range(10)])

class TileImage():
    def __init__(self, tiles):
        self.tiles = tiles
        self._neighbours = {}

    def neighbours(self, tile, use_cache = True):
        if not tile in  self._neighbours or not use_cache:
            self._neighbours[tile] = self._calculate_neighbours(tile)
        return self._neighbours[tile]

    def _calculate_neighbours(self, tile):
        neighbours = []
        for border in tile.borders():
            other_tiles = set(tiles) - set([tile])
            possible_neighbours = {other_tile: other_tile.possible_borders() for other_tile in other_tiles}
            neighbours.append(next(((n, possible_borders.index(border)) for n, possible_borders in possible_neighbours.items() if border in possible_borders), None))
        
        return neighbours

    def corners(self):
        corners = []
        for tile in self.tiles:
            neighbours = self.neighbours(tile)
            if len([n for n in neighbours if n]) == 2:
                corners.append(tile)

        return corners

    def is_inner(self, tile):
        neighbours = self.neighbours(tile)
        return len([n for n in neighbours if n]) == 4

    def align_tiles(self):
        processed = set()
        inner = next(tile for tile in tiles if self.is_inner(tile))
        inner.arrangement = 0
        to_process = [inner]

        while(processed) != set(self.tiles):
            current = to_process.pop()
            processed.add(current)
            for i, neighbour_with_type in enumerate(self.neighbours(current, False)):
                if neighbour_with_type != None:
                    n, type_of_match = neighbour_with_type
                    adjusted_neighbour = self._rearrange(n, i, type_of_match)
                    self.tiles[self.tiles.index(n)] = adjusted_neighbour
                    if adjusted_neighbour not in processed:
                        to_process.append(adjusted_neighbour)
    
    def generate_image(self):
        self.align_tiles()
        self._neighbours = {}

        image = []
        image_size = 8 * int(math.sqrt(len(self.tiles)))
        for i in range(image_size):
            image.append("")
        current = next(top_left_tile for top_left_tile in self.tiles if self.neighbours(top_left_tile)[0] == None and self.neighbours(top_left_tile)[3] == None)
        left = current
        for i in range(image_size):
            if i % 8 == 0 and i != 0: 
                current = self.neighbours(left)[2][0]
                left = current
            else:
                current = left

            for j in range(image_size):
                if j % 8 == 0 and j != 0:
                    current = self.neighbours(current)[1][0]
                image[i] += current.inner_content()[i%8][j%8]
        
        return image
    
    def _rearrange(self, subject, compared_edge, type_of_match):
        new_content = None
        subject_content_list = [list(r) for r in subject.content]

        if (compared_edge + 2) % 4 == type_of_match:
            new_content = subject_content_list
        elif (compared_edge, type_of_match) in [(0, 5),(1, 2), (2, 7), (3, 0)]:
            new_content = numpy.rot90(subject_content_list, 3).tolist()
        elif (compared_edge, type_of_match) in [(0, 4),(1, 5), (2, 6), (3, 7)]:
            new_content = numpy.rot90(subject_content_list, 2).tolist()
        elif (compared_edge, type_of_match) in [(0, 3),(1, 4), (2, 1), (3, 6)]:
            new_content = numpy.rot90(subject_content_list, 1).tolist()
        elif (compared_edge, type_of_match) in [(0, 6),(1, 1), (2, 4), (3, 3)]:
            new_content = numpy.fliplr(subject_content_list).tolist()
        elif (compared_edge, type_of_match) in [(0, 0),(1, 7), (2, 2), (3, 5)]:
            new_content = numpy.flipud(subject_content_list).tolist()
        elif (compared_edge, type_of_match) in [(0, 1),(1, 0), (2, 3), (3, 2)]:
            new_content = numpy.rot90(numpy.flipud(subject_content_list).tolist(), 3).tolist()
        elif (compared_edge, type_of_match) in [(0, 7),(1, 6), (2, 5), (3, 4)]:
            new_content = numpy.rot90(numpy.flipud(subject_content_list).tolist(), 1).tolist()

        new_content = ["".join(r) for r in new_content]
        return Tile(subject.id, new_content)

def data():
    def parse_tile(tile):
        return Tile(int(tile.split("\n")[0][5:-1]), tile.split("\n")[1:])

    with open("./day20/data", "r") as file:
        return [parse_tile(tile) for tile in file.read().split("\n\n")]

tiles = data()
tile_image = TileImage(tiles)
print(math.prod([c.id for c in tile_image.corners()]))

def possible_images(image):
    image = [list(r) for r in image]
    return [
        image,
        numpy.rot90(image, 3).tolist(),
        numpy.rot90(image, 2).tolist(),
        numpy.rot90(image, 1).tolist(),
        numpy.fliplr(image).tolist(),
        numpy.flipud(image).tolist(),
        numpy.rot90(numpy.flipud(image).tolist(), 3).tolist(),
        numpy.rot90(numpy.flipud(image).tolist(), 1).tolist()
    ]

def match_sea_monster(possible_images):
    sea_monster = [(0, 18), (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1,17), (1,18), (1,19), (2, 1), (2, 4), (2, 7), (2,10), (2, 13), (2, 16)]
    count_of_sea_mosters = {}
    for image_variant, image in enumerate(possible_images):
        count = 0
        for i in range(len(image) - 2):
            for j in range(len(image) - 19):
                present = True
                for coord in sea_monster:
                    if image[coord[0] + i][coord[1] + j] != "#":
                        present = False
                if present == True:
                    count += 1
        count_of_sea_mosters[image_variant] = count
    return count_of_sea_mosters.values()

actual_image = tile_image.generate_image()
count_of_hash = "".join(actual_image)
print(count_of_hash.count("#") - 15 * max(match_sea_monster(possible_images(tile_image.generate_image()))))