class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build the indegree and adjacency list 
        # topological sort 
        # bfs -> visit node with an indegree of 0
        # record node 
        # iterate through the adjacency list, decrement the indegree of 
        # each neighbour in the adjacency list 
        # if a neighbour has an indegree of 0, add it to the queue 
        # return final ans 

        indegree = [0] * numCourses 
        adj = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            indegree[course] += 1 # course has one more dependency
            adj[prereq].append(course) # prereq -> course
        
        # populate q with courses w no prereqs 
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        # run bfs for topological sort
        ans = []
        while q:
            course = q.popleft()
            ans.append(course)
            for nei in adj[course]:
                indegree[nei] -= 1 
                if indegree[nei] == 0:
                    q.append(nei)

        if len(ans) == numCourses:
            return ans 
        else:
            return []