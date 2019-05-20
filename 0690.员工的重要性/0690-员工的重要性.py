"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, i):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        res = 0
        hashmap = dict()
        
        for employee in employees:
            hashmap[employee.id] = [employee.importance, employee.subordinates]
        
        queue = [i]
        while(queue):
            next_queue = []
            for item in queue:
                res += hashmap[item][0]
                next_queue += hashmap[item][1] #把下属列表加入下一次的queue                
            queue = next_queue[:]
            
        return res