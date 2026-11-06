from pathlib import Path

from ament_flake8.main import main_with_errors


def test_flake8():
    package = Path(__file__).resolve().parents[1]
    result, errors = main_with_errors(argv=[str(package)])
    assert result == 0, '\n'.join(errors)
