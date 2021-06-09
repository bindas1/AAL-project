class Node:

    def __init__(self, top, left, length, width):
        # przestrzen ktora zajmuje root
        self.top = top
        self.left = left
        self.length = length
        self.width = width

        # dzieci
        self.left_child = None
        self.right_child = None

        self.free = True  # czy przestrzen zajęta przez jakiś klocek

    def insert(self, box):

        # jeśli box dokładnie pasuje do node
        if self.free and box[0] == self.length and box[1] == self.width:
            self.free = False
            return box[2]

        # jeśli box jest większy niż node
        elif box[0] > self.length or box[1] > self.width:
            return None

        # jeśli zostaje szerszy pas w szerokości niż w długości
        elif self.width - box[1] > self.length - box[0]:
            # dzielimy na dwa pionowe węzły
            if self.left_child is None:
                self.left_child = Node(self.top, self.left, self.length / 2, self.width)
            if self.right_child is None:
                self.right_child = Node(self.top, self.left + self.length / 2, self.length / 2, self.width)

        else:
            # dzielimy na dwa poziome węzły
            if self.left_child is None:
                self.left_child = Node(self.top, self.left, self.length, self.width / 2)
            if self.right_child is None:
                self.right_child = Node(self.top + self.width / 2, self.left, self.length, self.width / 2)

        new_node_left = self.left_child.insert(box)

        if new_node_left is None:
            new_node_right = self.right_child.insert(box)
            if new_node_right is None:
                self.free = False
                return box[2]

