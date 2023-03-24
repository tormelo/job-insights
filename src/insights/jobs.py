from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(reader)


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)

    job_types_set = {job["job_type"] for job in jobs}

    return list(job_types_set)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]
