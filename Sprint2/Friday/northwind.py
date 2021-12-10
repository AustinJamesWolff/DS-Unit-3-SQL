"""Pull queries on our northwind data."""

import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()


def get_query(query):
    """Get query."""
    results = curs.execute(query).fetchall()
    conn.commit()
    return results


get_expensive_items = """
    SELECT *
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;
"""

expensive_items = get_query(get_expensive_items)
# print("Expensive items:", expensive_items)


avg_age = """
    SELECT AVG(HireDate - BirthDate)
    FROM Employee;
"""

avg_hire_age = get_query(avg_age)
# print("Average age of hiring:", avg_hire_age)


avg_age_by_city = """
    SELECT City, AVG(HireDate - BirthDate)
    FROM Employee
    GROUP BY City;
"""

avg_age_by_city = get_query(avg_age_by_city)
# print("Average age of hiring by city:", avg_age_by_city)


get_10_most_exp = """
    SELECT Product.ProductName, Product.UnitPrice,
    Supplier.CompanyName
    FROM Product
    INNER JOIN Supplier
        ON Product.SupplierId = Supplier.Id
    ORDER BY UnitPrice DESC
    LIMIT 10;
"""

ten_most_expensive = get_query(get_10_most_exp)
# print("Ten most expensive and supplier:", ten_most_expensive)


get_largest_cat = """
    SELECT CategoryName, COUNT(DISTINCT ProductName)
    FROM Category
    INNER JOIN Product
        ON Category.Id = Product.CategoryId
    GROUP BY CategoryName
    ORDER BY COUNT(DISTINCT ProductName) DESC
    LIMIT 1;
"""

largest_category = get_query(get_largest_cat)
print("Largest category:", largest_category)

get_most_terr = """
      SELECT EmployeeId, FirstName, LastName,
      COUNT(DISTINCT TerritoryId) AS Territories
      FROM EmployeeTerritory
      INNER JOIN Employee
        ON EmployeeTerritory.EmployeeId = Employee.Id
      GROUP BY EmployeeId
      ORDER BY Territories DESC
      LIMIT 1;
"""

most_territories = get_query(get_most_terr)
# print("Most territories:", most_territories)
