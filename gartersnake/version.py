import subprocess
import sys

from gartersnake.pip import installed_packages


def vcs_version() -> str:
    try:
        if 'dunamai' not in installed_packages():
            subprocess.run(
                f'{sys.executable} -m pip install dunamai',
                shell=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

        from dunamai import Version

        version = Version.from_any_vcs().serialize()
    except (ModuleNotFoundError, RuntimeError) as error:
        print(error)
        version = '0.0.0'

    return version
