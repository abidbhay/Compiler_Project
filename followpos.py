import build_tree as tree
import pos_traversal as pos
root=tree.root
leaves=pos.leaves
fp_arr = [[] for _ in range(leaves)]
#print(fp_arr)

def traversal(root,head):
    global i, symbols, fp_arr
    if head.left==None:
        #leaf node
        #print(head.val)
        return head.val


    traversal(root, head.left)
    if head.val!='*':
        traversal(root, head.right)
    #print(head.val)
    if (head.val=='*'):
        #print(head.lastpos)

        for q in head.firstpos:
            #print(q)
            #print(fp_arr[q])
            #print(head.lastpos)
            for i in head.lastpos:
                if i not in fp_arr[q]:
                    fp_arr[q].append(i)
            #print(fp_arr)

            #print(head.firstpos)

    elif head.val =='#':
        pass

    elif (head.val=='.'):
        #print(head.left.lastpos)
        for m in head.left.lastpos:
            #print(m)
            #print(len(fp_arr))
            if head.right.lastpos not in fp_arr[m]:
                for i in head.right.lastpos:
                    fp_arr[m].append(i)
                #print(fp_arr)
            #print(fp_arr[m])

            #print(head.right.firstpos)

def print_followpos_table(followpos_arr):
    #print(followpos_arr)
    n=len(followpos_arr)
    print(f"Position |  Followpos ")
    for i in range(1,n):
        temp=followpos_arr[i]
        if i==n-1:
            temp='#'
        print("  "+str(i)+ "            "+ str(temp))

#driver code

symbols = tree.symbols
head=root
traversal(root,head)
print_followpos_table(fp_arr)
print(fp_arr)