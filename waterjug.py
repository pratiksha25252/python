from collections import deque
def water_jug_problem(jug1_capacity,jug2_capacity,target):
    visited=set()
    #queue for bfs
    queue=deque()
    #initaial stste:both jugs are empty
    initial_state=(0,0)
    queue.append((0,0))
    #store the path to reach the solution
    path={}
    path[initial_state]=None
    while queue:
        current_state=queue.popleft()
        jug1,jug2=current_state
        #if we reach the target
        if jug1==target or jug2==target:
            solution_path=[]
            while current_state:
                solution_path.append(current_state)
                current_state =path[current_state]
            solution_path.reverse()
            return solution_path
    # skip if this state is already visited
        if current_state in visited:
            continue
        #mark the current state as visited
        visited.add(current_state)
        
        #possible actions
        possible_states=[
            (jug1_capacity,jug2),
            #fill jug1
            (jug1,jug2_capacity), #fill jug2
            (0,jug2),
            (jug1,0),
            #pour jug2->jug1
            (min(jug1_capacity,jug1 +jug2),max(0,jug2-(jug1_capacity -jug1))),
            (max(0,jug1-(jug2_capacity -jug2)), min(jug2_capacity,jug1+jug2)),
        ]           
        for states in possible_states:
            if states not in visited:
                queue.append(states)
                path[states]=current_state
                
    return None #no solution
#Example usage
if __name__== "__main__":
    jug1_capacity=4
    jug2_capacity=3
    target=2
    solution=water_jug_problem(jug1_capacity,jug2_capacity,target)
    if solution:
        print("solution found")
        for step in solution:
            print(step)
    else:
        print("no solution")
    