SELECT D.name as Department, 
	   E.name as Employee, 
	   e.Salary as Salary
From EmplOyeE as E 
     INNER JOIN 
     Department as D
ON E.DepartmentId = D.ID and
   e.SALARY = (SELECT MAX(SALARY)
                FROM EMPLOYEE 
                WHERE DEPARTMENTID = D.ID)