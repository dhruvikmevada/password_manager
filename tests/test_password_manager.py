try:
    import pytest
except ModuleNotFoundError as e:
    print(
        "Module Missing! Install "
        f"dependencies from requirement.txt file: {e.name}"
    )


@pytest.fixture()
def temporary_function():
    # TODO
    pass
