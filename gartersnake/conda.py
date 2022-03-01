from pathlib import Path
import subprocess
import sys
from typing import List

from gartersnake.dependencies import dependency_tree
from gartersnake.missing import missing_requirements


def is_conda() -> bool:
    return (Path(sys.prefix) / 'conda-meta').exists()


def install_conda_requirements(requirements: List[str] = None, channel: str = None, overwrite: bool = False):
    if channel is None:
        channel = 'conda-forge'

    if is_conda():
        print(f'found conda environment at {sys.prefix}')
    else:
        raise EnvironmentError('conda environment not detected')

    if overwrite:
        missing_packages = requirements
    else:
        missing_packages = missing_requirements(requirements)

    if channel is not None:
        conda_install_command = f'conda install -c {channel} -y {" ".join(missing_packages)}'
    else:
        conda_install_command = f'conda install -y {" ".join(missing_packages)}'

    conda_packages = []
    non_conda_packages = []
    try:
        subprocess.check_output(
            conda_install_command,
            shell=True,
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError as error:
        output = error.output.decode()
        package_not_found_start = 'PackagesNotFoundError: The following packages are not available from current channels:\n\n'
        package_not_found_stop = '\n\nCurrent channels:'
        if package_not_found_start in output:
            non_conda_packages = [
                package.strip().strip('-').strip()
                for package in output[
                               output.index(package_not_found_start): output.index(
                                   package_not_found_stop
                               )
                               ].splitlines()[2:]
            ]

            print(
                f'found {len(conda_packages)} conda packages (out of {len(missing_packages)}) - {conda_packages}'
            )

            non_conda_dependency_tree = dependency_tree(*non_conda_packages)
            for non_conda_dependencies in non_conda_dependency_tree.values():
                if len(non_conda_dependencies) > 0:
                    install_conda_requirements(non_conda_dependencies)
                    missing_packages = missing_requirements(requirements)

            conda_packages = [
                package
                for package in missing_packages
                if not any(
                    non_conda_package in package for non_conda_package in non_conda_packages
                )
            ]

    if channel is not None:
        conda_install_command = f'conda install -c {channel} -y {" ".join(conda_packages)}'
    else:
        conda_install_command = f'conda install -y {" ".join(conda_packages)}'

    try:
        subprocess.run(
            conda_install_command,
            shell=True,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        pass
