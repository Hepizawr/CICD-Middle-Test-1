import pytest


@pytest.fixture(autouse=True)
def file_fixture():
    with open("fixture_file", 'w') as file:
        lines = ['1 Bob Simson 20.00$ decorations\n',
                 '2 Mary 30.00$ food\n',
                 '3 Mary 40.00$ toys\n',
                 '4 Aleksa 50.00$ drinks\n',
                 '5 Aleksa 60.00$ accessories\n',
                 '6 Mary 70.00$ accessories\n',
                 '7 Bob Simson 80.00$ drinks\n',
                 '8 Bob Simson 90.00$ instruments\n',
                 '9 Aleksa 60.00 Accessories\n',
                 '10 Mary 100.00$ accessories\n'
                 ]
        file.writelines(lines)
    return "fixture_file"
