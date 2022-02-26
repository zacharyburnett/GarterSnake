from gartersnake.missing import missing_requirements


def test_check_missing_requirements():
    test_packages = ['dunamai', 'requests']

    missing_packages = missing_requirements(test_packages)

    assert missing_packages == ['requests']
