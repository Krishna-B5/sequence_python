import os
import pytest

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"
