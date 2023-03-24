from typing import Union, List, Dict
from src.insights.jobs import read


def get_salaries(path: str) -> list[int]:
    jobs = read(path)

    max_salaries_set = {job["max_salary"] for job in jobs}
    min_salaries_set = {job["min_salary"] for job in jobs}
    salaries_set = min_salaries_set.union(max_salaries_set)

    return [int(salary) for salary in salaries_set if salary.isnumeric()]


def get_max_salary(path: str) -> int:
    return max(get_salaries(path))


def get_min_salary(path: str) -> int:
    return min(get_salaries(path))


def convert_to_int(input: Union[int, str]) -> int:
    input_type = type(input)

    if input_type == int:
        return input
    elif input_type == str and input.isnumeric():
        return int(input)
    else:
        raise ValueError("Invalid value")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if ("min_salary" not in job) or ("max_salary" not in job):
        raise ValueError("Expected key doesn't exist")

    min_salary = convert_to_int(job["min_salary"])
    max_salary = convert_to_int(job["max_salary"])
    target = convert_to_int(salary)

    if min_salary > max_salary:
        raise ValueError("min_salary can't be greater than max_salary")

    return min_salary <= target <= max_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
