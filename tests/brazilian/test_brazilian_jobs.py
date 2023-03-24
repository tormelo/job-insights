from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    translated_list = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    expected_keys = ["title", "salary", "type"]

    for job in translated_list:
        for key in expected_keys:
            assert key in job
