class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    def insert(self, value):
        if value <= self.value:
            if self.left is None:
                self.left = Node(value)
                return
            self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
                return
            self.right.insert(value)

    def print_sym(self):
        # print left
        if self.left is not None:
            self.left.print_sym()

        # print self
        print(self.value, end=' ')

        # print right
        if self.right is not None:
            self.right.print_sym()

    def print_rev(self):
        # print left
        if self.left is not None:
            self.left.print_sym()

        # print right
        if self.right is not None:
            self.right.print_sym()

        # print self
        print(self.value, end=' ')



class BST:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def print_sym(self):
        self.root.print_sym()
        print()

    def print_rev(self):
        self.root.print_rev()
        print()

    def print_struct(self):
        queue = [(self.root, 0)]
        cur_height = 0
        while queue:
            node, height = queue.pop(0)
            if height > cur_height:
                cur_height = height
                print()
            if node is None:
                print('_', end=' ')
                continue
            print(node.value, end=' ')
            queue.append((node.left, cur_height + 1))
            queue.append((node.right, cur_height + 1))

    def print_specific_level(self, level):
        queue = [(self.root, 0)]
        found = False
        while queue:
            node, height = queue.pop(0)
            if height == level:
                found = True
                if node is None:
                    print('_', end=' ')
                else:
                    print(node.value, end=' ')
            elif height < level:
                if node is not None:
                    queue.append((node.left, height + 1))
                    queue.append((node.right, height + 1))

        if not found:
            print(f"Level {level} does not exsist")




def bts_research(bst, nums):
    turtle = [(0, len(nums) - 1)]
    while turtle:
        ninja, knight = turtle.pop(0)
        middle = (ninja + knight) // 2
        bst.insert(nums[middle])
        if knight != ninja:
            if middle != ninja:
                turtle.append((ninja, middle -1))
            if middle != knight:
                turtle.append((middle + 1, knight))

print('Enter your set')

bst = BST()
values = sorted([int(it) for it in input().split()])
bts_research(bst, values)
print('Chose the way you would like to show your BTS: symmetric (sym), reversive (rev), the structure (struct) or what elements in the level')
way = input()
if way == 'sym':
    bst.print_sym()
elif way == 'rev':
    bst.print_rev()
elif way == 'struct':
    bst.print_struct()
elif way == 'level':
    print('Enter level')
    level = int(input())
    bst.print_specific_level(level)
else:
    print('Invalid command')



