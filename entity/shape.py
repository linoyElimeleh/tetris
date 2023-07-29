class Shape:
    def __init__(self, letter, matrix):
        self.letter = letter
        self.matrix = matrix
        self.height = len(matrix)
        self.width = len(matrix[0])

    def __str__(self):
        return f"Shape: {self.letter}, Size: {self.height}x{self.width}"


T = Shape('T', [['T', 'T', 'T'],
                ['', 'T', '']])

S = Shape('S', [['', 'S', 'S'],
                ['S', 'S', '']])

Z = Shape('Z', [['Z', 'Z', ''],
                ['', 'Z', 'Z']])

J = Shape('J', [['', 'J'],
                ['', 'J'],
                ['J', 'J']])

L = Shape('L', [['L', ''],
                ['L', ''],
                ['L', 'L']])

I = Shape('I', [['I', 'I', 'I', 'I']])

Q = Shape('Q', [['Q', 'Q'],
                ['Q', 'Q']])

tetris_shapes = {
    'T': T,
    'S': S,
    'Z': Z,
    'J': J,
    'L': L,
    'I': I,
    'Q': Q
}


def match_entity_to_shape_object(entity):
    return tetris_shapes.get(entity)
