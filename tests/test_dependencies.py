from gartersnake.dependencies import dependency_tree


def test_dependency_tree():
    tree = dependency_tree('requests', 'numpy', 'pyproj', 'adcircpy')

    assert list(tree) == ['adcircpy']
