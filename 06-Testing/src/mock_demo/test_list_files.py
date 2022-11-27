
from unittest import mock
from list_files import list_files

def test_list_files(mocker):
    mock.patch.object('subprocess.run', return_value='foo')
    assert list_files() == 'foo'
