from src.pre_built.sorting import sort_by
from src.insights.jobs import read


def test_sort_by_criteria():
    jobs = read("data/jobs.csv")
    assert jobs[0]["id"] == "0"

    sort_by(jobs, "min_salary")
    assert jobs[0]["id"] == "2191"

    sort_by(jobs, "max_salary")
    assert jobs[0]["id"] == "2105"

    sort_by(jobs, "date_posted")
    assert jobs[0]["id"] == "7"
