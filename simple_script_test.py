"""This is literaly simplest example of a test script"""

from simple_script import add_numbers


def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(1, 2) == 3
