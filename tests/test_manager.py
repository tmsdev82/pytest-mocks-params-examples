from src import manager
from unittest import mock
import pytest

def test_manager_init():
    with mock.patch.object(manager, "main", return_value=1) as mock_main:
        with mock.patch.object(manager, "__name__", "__main__"):
            with mock.patch.object(manager.sys, "exit") as mock_exit:
                manager.init()

                mock_main.assert_called()
                assert mock_exit.call_args[0][0] == 1

@pytest.mark.parametrize("concat_files_text_return, expected_result", [("pie", 3), (None, None)])
@mock.patch("src.manager.file_utils.concat_files_text")
def test_manager_main(mock_concat_files_text, concat_files_text_return, expected_result):    
    mock_concat_files_text.return_value = concat_files_text_return

    actual_result = manager.main()    

    mock_concat_files_text.assert_called()
    assert actual_result == expected_result