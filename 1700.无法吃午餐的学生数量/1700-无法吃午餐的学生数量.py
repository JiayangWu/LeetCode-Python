class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque
        students = deque(students)
        while sandwiches:
            cur, l = 0, len(students)
            while cur < l:
                student = students.popleft()
                if student == sandwiches[0]:
                    break
                students.append(student)
                cur += 1
            if cur == l:
                break
            sandwiches = sandwiches[1:]
        return len(students)