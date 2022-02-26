from gartersnake.pip import installed_packages


def test_installed_packages():
    packages = installed_packages()

    reference_packages = ['dunamai', 'pip', 'setuptools']
    assert all(package in packages for package in reference_packages)
