import followpos as fp
import build_tree as tree
regex =tree.string
symbols= tree.symbols
pthesis= tree.pthesis
fparr= fp.fp_arr
root=tree.root
head=root
queue=[]


finite_automata={}
point=1
regex_dict={}
dfa_inputs=[]
for i in regex:
    if i not in pthesis and i not in symbols and i!='#':
        regex_dict[point]=i
        point+=1
        if i not in dfa_inputs:
            dfa_inputs.append(i)
s=0
initial_state=head.firstpos
accept_states=[]
queue.append(head.firstpos)
while queue:
    if s>len(queue)-1:
        break
    curr_state=queue[s]
    s+=1
    curr_state=tuple(curr_state)
    if curr_state not in finite_automata:
        finite_automata[curr_state] = {}
        #notvisited[curr_state]=1
    else:
        continue
        #notvisited[curr_state]=0
    temp={}
    flag=False
    for i in dfa_inputs:
        inter_state=[]
        for j in curr_state:
            if j not in regex_dict:
                continue
            value=regex_dict[j]
            if i==value:
                #print(value,j)
                #print(fparr[j])
                for k in fparr[j]:
                    inter_state.append(k)
                    if k==len(regex_dict)+1:
                        flag=True
        #print(inter_state)
        if flag:
            accept_states.append(inter_state)
        if inter_state not in queue:
            queue.append(tuple(inter_state))
        temp[i]=inter_state
    finite_automata[curr_state]=temp
print(finite_automata)
#print(dfa_inputs)
#print(regex_dict)
print(accept_states)