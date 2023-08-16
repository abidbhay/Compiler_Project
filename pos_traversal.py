import build_tree as tree
root=tree.root
i=1
def traversal(root,head):
    global i, symbols
    if head.left==None:
        #leaf node
        head.firstpos.append(i)
        head.lastpos.append(i)
        #print(head.val)
        #print(head.val,end=f' fp:{head.firstpos}, lp:{head.lastpos} ,')
        i+=1
        return head.val

    traversal(root, head.left)
    if head.val!='*':
        traversal(root, head.right)
    #print(head.val,end='')
    if head.val in symbols:
        if head.val=='|':
            head.firstpos=head.left.firstpos + head.right.firstpos
            head.lastpos= head.left.lastpos + head.right.lastpos
        if head.val=='*':
            head.nullable=1
            head.firstpos=head.left.firstpos
            head.lastpos = head.left.lastpos
        if head.val=='.':
            if(head.left.nullable==1):
                head.firstpos=head.left.firstpos+head.right.firstpos
            else:
                head.firstpos=head.left.firstpos
            if (head.right.nullable==1):
                head.lastpos=head.left.lastpos+head.right.lastpos
            else:
                head.lastpos=head.right.lastpos
    #print(head.firstpos,end=",")  #verify if fpos and lpos yield correct results
    #print(head.lastpos, end=",")  # verify if fpos and lpos yield correct results


#driver code

symbols = tree.symbols
head=root
traversal(root,head)
leaves=i
