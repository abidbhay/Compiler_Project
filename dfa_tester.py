import dfa_creator as fa

dfa=fa.finite_automata
initial= fa.initial_state
accept_states=fa.accept_states
test_str='aaabb'
curr=tuple(initial)
for symbol in test_str:
    curr = dfa[curr][symbol]
    curr=tuple(curr)


flag=False
for i in accept_states:
    i=tuple(i)
    if curr==i:
        flag=True
        print("String accepted")
        break
if flag==False:
    print("Rejected")