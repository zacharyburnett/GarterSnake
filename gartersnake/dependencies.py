from functools import lru_cache
import re
from typing import Dict, List

import johnnydep


@lru_cache(maxsize=None)
def dependency_tree(*requirements) -> Dict[str, List[str]]:
    dependencies = {}
    pattern = re.compile('[<>=~]=?.*')
    for requirement in requirements:
        for children in dependencies.values():
            if requirement in children:
                continue
        children = [
            re.sub(pattern, '', child) for child in johnnydep.JohnnyDist(requirement).requires
        ]
        for dependency in list(dependencies):
            if dependency in children:
                del dependencies[dependency]
        dependencies[requirement] = children

    return dependencies
