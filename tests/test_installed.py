from gartersnake import missing_requirements
from gartersnake.pip import installed_packages


def test_installed_packages():
    existing_packages = ['pip', 'setuptools']
    nonexisting_packages = ['pydantic', 'nonexistent']

    installed = installed_packages()

    assert all(package in installed for package in existing_packages)
    assert all(package not in installed for package in nonexisting_packages)


def test_missing_requirements():
    existing_packages = ['pip', 'setuptools']
    nonexisting_packages = ['pydantic', 'nonexistent']

    missing = missing_requirements(existing_packages + nonexisting_packages)

    assert all(package in missing for package in nonexisting_packages)
