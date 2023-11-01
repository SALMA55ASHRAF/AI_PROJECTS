def DFS(m):
    start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    while len(frontier)>0:
        currCell=frontier.pop()
        if currCell==(1,1):#goal
            break
        # expand our node to next
        for d in "ESNW":
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childcell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childcell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childcell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childcell=(currCell[0]-1,currCell[1])
                if childcell in explored:
                    continue
                explored.append(childcell)
                frontier.append(childcell)
                dfspath[childcell]=currCell
    fwd={}
    cell=(1,1)
    while cell!=start:
        fwd[dfspath[cell]]=cell
        cell=dfspath[cell]
    return fwd