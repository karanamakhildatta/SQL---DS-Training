1.1 What is a Database?
A database is an organized collection of structured data stored electronically. Think of it like a sophisticated Excel workbook where data is stored in tables (like sheets), and each table has rows (records) and columns (fields).
Key Terms:

- Table: A collection of related data organized in rows and columns
- Row (Record): A single entry in a table representing one item
- Column (Field): A specific attribute or property of the data
- Primary Key: A unique identifier for each row (like a roll number for students)

  1.2 SELECT Statement
  The SELECT statement retrieves data from a database. It's the most commonly used SQL command.

Basic Syntax:

```sql
SELECT column1, column2, ...
FROM table_name;
```

Example:

```sql
-- Select specific columns
SELECT name, salary
FROM employees;

-- Select all columns using *
SELECT *
FROM employees;

-- Select with column alias (renaming output)
SELECT name AS employee_name, salary AS annual_salary
FROM employees;
```

1.3 WHERE Clause
The WHERE clause filters records based on specified conditions.

Basic Syntax:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

Comparison Operators:

| Operator | Description              | Example              |
| -------- | ------------------------ | -------------------- |
| =        | Equal to                 | WHERE age = 30       |
| <> / !=  | Not equal to             | WHERE age <> 30      |
| >        | Greater than             | WHERE salary > 50000 |
| <        | Less than                | WHERE salary < 50000 |
| >=       | Greater than or equal to | WHERE age >= 18      |
| <=       | Less than or equal to    | WHERE age <= 65      |

Examples:

```sql
-- Select employees with salary greater than 50000
SELECT name, salary
FROM employees
WHERE salary > 50000;

-- Select employees from a specific department
SELECT name, department
FROM employees
WHERE department = 'Sales';

-- Select employees older than 30
SELECT name, age
FROM employees
WHERE age > 30;

-- Find employees who are NOT in HR
SELECT name, department
FROM employees
WHERE department != 'HR';

-- Find employees hired after 2020
SELECT name, hire_date
FROM employees
WHERE hire_date > '2020-01-01';
```

1.4 Combining Conditions

You can combine multiple conditions in the WHERE clause using **AND**, **OR**, and **NOT** operators.

Basic Syntax:

```sql
-- AND: Both conditions must be true
SELECT *
FROM employees
WHERE department = 'Engineering' AND salary > 70000;

-- OR: At least one condition must be true
SELECT *
FROM employees
WHERE department = 'Engineering' OR department = 'Marketing';

-- NOT: Negates the condition
SELECT *
FROM employees
WHERE NOT department = 'HR';

-- Combining multiple operators
SELECT *
FROM employees
WHERE (department = 'Engineering' OR department = 'Marketing')
  AND salary > 60000;
```

### 1.5 Practice Exercise

1. Write a query to select the names and salaries of employees who has salary greater than 25000 and work in the 'Sales' department.
```sql
SELECT name, salary FROM employees WHERE salary > 25000 AND department = "Sales";
```
2. Write a query to find all employees with a salary less than 40000 or who were hired before 2019.
```sql
SELECT * FROM `employees` WHERE salary < 40000 or hire_date <= '2018-12-31';
```
```sql
SELECT * FROM `employees` WHERE salary < 40000 or hire_date < '2019-01-01';
```
Questions for Practice:

1. Write a query to select the product names and prices of products that belong to the 'Electronics' category and have a price greater than 100.
 ```sql
 SELECT product_name, price FROM `products` WHERE category = 'Electronics' and price > 100;
```
2. Write a query to find all products that are either out of stock (stock = 0) or have a price less than 50.
```sql
SELECT * FROM `products` WHERE stock = 0 OR price < 50;
```
3. Write a query to select all products that do not belong to the 'Decor' category.
```sql
SELECT * FROM `products` WHERE `category` <> 'Decor';
```
4. Write a query to select all products that have a price between 50 and 150 (inclusive).
