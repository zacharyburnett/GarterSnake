import pytest as pytest

from gartersnake.conda import install_conda_requirements, is_conda
from gartersnake.pip import installed_packages


@pytest.mark.skipif(not is_conda(), reason='requires an Anaconda environment')
def test_install_conda_requirements():
    test_packages = ['numpy', 'xarray', 'adcircpy']

    assert not any(test_package in installed_packages() for test_package in test_packages)

    install_conda_requirements(test_packages)

    assert all(test_package in installed_packages() for test_package in test_packages)
