import pytest

from gartersnake.conda import is_conda
from gartersnake.pip import installed_packages
from gartersnake.windows import install_windows_requirements, is_windows


@pytest.mark.skipif(not is_windows() or is_conda(), reason='requires a Windows environment')
def test_install_windows_requirements():
    test_packages = ['numpy', 'xarray']

    assert not any(test_package in installed_packages() for test_package in test_packages)

    install_windows_requirements(test_packages)

    assert all(test_package in installed_packages() for test_package in test_packages)
