from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
    def is_valid(self, visited_stack, x, y):
        if (x<0) or (x>=len(self.navigator_maze)) or (y<0) or (y>=len(self.navigator_maze[0])) or (self.navigator_maze[x][y]==1) or (visited_stack.is_in(x, y)):
            return False
        else:
            return True
            
        
    def find_path(self, start, end):
        # IMPLEMENT FUNCTION HERE
        path_stack= Stack()
        visited_stack=Stack()
        
        if self.navigator_maze[start[0]][start[1]]==1 or self.navigator_maze[end[0]][end[1]]==1:
            
            raise PathNotFoundException
            
            
        else:
            path_stack.push(start[0],start[1])
            visited_stack.push(start[0],start[1])
            current=start
            while (current != end) and (path_stack.length() != 0):
                
                q=current[0]
                w=current[1]
                U=(q-1,w)
                D=(q+1,w)
                L=(q,w-1)
                R=(q,w+1)
                if self.is_valid(visited_stack,U[0],U[1]):
                    path_stack.push(U[0],U[1])
                    visited_stack.push(U[0],U[1])
                    current=U
                elif self.is_valid(visited_stack,D[0],D[1]):
                    path_stack.push(D[0],D[1])
                    visited_stack.push(D[0],D[1])
                    current=D
                elif self.is_valid(visited_stack,R[0],R[1]):
                    path_stack.push(R[0],R[1])
                    visited_stack.push(R[0],R[1])
                    current=R
                elif self.is_valid(visited_stack,L[0],L[1]):
                    path_stack.push(L[0],L[1])
                    visited_stack.push(L[0],L[1])
                    current=L
                else:
                    path_stack.pop_ele()
                    o=path_stack.length()
                    current=path_stack.return_last()
                    

                
            if path_stack.length()!=0:
                l=path_stack.print_stack()
                print(l)
                return l
                
            else:
                raise PathNotFoundException
                
            
                
            
                
            


