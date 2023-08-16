class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.firstpos=[]
        self.lastpos=[]
        if val=='*':
            self.nullable=1
        else:
            self.nullable=0
    @staticmethod
    def makeNode(i, string, root, symbol=True):
        if symbol == True:
            symbol = string[i]
            if (symbol!='*'):
                right = string[i + 1]
            else:
                right=None
            left = string[i - 1]
        else:
            symbol = "."
            left = string[i - 1]
            right = string[i]
        node = Node(symbol)
        node.left, node.right = Node(left), Node(right)
        if root == None:
            root = node
        else:
            temp = root
            root = node
            root.left = temp
        i += 1
        return root

    @staticmethod
    def build(i, n, root, string, queue):
        global symbols, pthesis, alphrange

        while i < n:
            char = string[i]

            if char == pthesis[0]:
                queue.append(char)
                i += 1
                continue
            elif char != pthesis[1] and queue:
                queue.append(char)
            elif char == pthesis[1] and queue:
                queue.append(char)
                queue.pop(0)
                queue.pop()
                q = len(queue)
                root = Node.build(0, q, root, queue, [])
                queue = []
            else:
                temp = string
                if queue:
                    temp = str(queue)
                    queue = []
                if char in symbols:
                    root = Node.makeNode(i, temp, root, True)

                else:
                    if (i > 0) and string[i - 1] not in symbols:
                        root = Node.makeNode(i, temp, root, False)
                    if (i>0 and string[i-1]=='*'):
                        root = Node.makeNode(i, temp, root, False)

            i += 1

        return root


# Driver Code
string = "(a|b)*abb#"
symbols = ['|', '*', '+','.']
pthesis = ['(', ')']
queue = []
i = 0
n = len(string)
root = None
root = Node.build(i, n, root, string, queue)
