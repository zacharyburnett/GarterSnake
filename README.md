# GarterSnake

[![tests](https://github.com/zacharyburnett/GarterSnake/workflows/tests/badge.svg)](https://github.com/zacharyburnett/GarterSnake/actions?query=workflow%3Atests)
[![build](https://github.com/zacharyburnett/GarterSnake/workflows/build/badge.svg)](https://github.com/zacharyburnett/GarterSnake/actions?query=workflow%3Abuild)
[![version](https://img.shields.io/pypi/v/GarterSnake)](https://pypi.org/project/GarterSnake)
[![license](https://img.shields.io/github/license/zacharyburnett/GarterSnake)](https://opensource.org/licenses/MIT)
[![style](https://sourceforge.net/p/oitnb/code/ci/default/tree/_doc/_static/oitnb.svg?format=raw)](https://sourceforge.net/p/oitnb/code)

GarterSnake is a set of functions that helps with using `setuptools` in
`setup.py`. It includes

- dynamically retrieving version info from VCS with `dunamai`
- installing packages from [Christoph Gohlke's Windows binaries](https://www.
  lfd.uci.edu/~gohlke/pythonlibs/) with `pipwin`
- installing packages using `conda`

## Usage

```python
from setuptools import find_packages, setup

from gartersnake import install_conda_requirements, install_windows_requirements, is_conda, is_windows, missing_requirements, vcs_version

REQUIREMENTS = {
    'fiona': ['gdal'],
    'numpy': [],
    'requests': [],
}

MISSING = missing_requirements(REQUIREMENTS)
if is_conda():
    install_conda_requirements(MISSING)
    MISSING = missing_requirements(REQUIREMENTS)
if is_windows():
    install_windows_requirements(MISSING)

__version__ = vcs_version()

setup(
    name='<package_name>',
    version=__version__,
    authors='<package_authors>',
    url='<package_url>',
    packages=find_packages(),
    python_requires='>=3.6',
    setup_requires=['dunamai', 'setuptools>=41.2'],
    install_requires=list(REQUIREMENTS),
)
```