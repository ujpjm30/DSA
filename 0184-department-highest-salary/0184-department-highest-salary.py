import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    result = employee.merge(department, left_on="departmentId", right_on="id")

    result["max_salary"] = result.groupby("name_y")["salary"].transform("max")

    result = result[result["salary"] == result["max_salary"]]

    result = result[["name_y", "name_x", "salary"]]

    result = result.rename(columns={

        "name_y": "Department",

        "name_x": "Employee",

        "salary": "Salary"

    })

    return result
    