from src import file_utils
from unittest import mock


def get_file_text_side_effect(file_path: str) -> str:
    file_texts = {
        "test1.txt": "hi\ntester",
        "test2.txt": "ho"
    }
    return file_texts.get(file_path)

def test_concat_file():
    with mock.patch("src.file_utils.Path.rglob", return_value=["test1.txt", "test2.txt"]):
        with mock.patch("src.file_utils.get_file_text", side_effect=get_file_text_side_effect) as mock_get_file_text:

            expected_result = "hi\ntester ho"
            actual_result = file_utils.concat_files_text("./data", ".txt")

            mock_get_file_text.assert_has_calls([mock.call("test2.txt"),mock.call("test1.txt")], any_order=True)
            assert expected_result == actual_result

def test_get_file_text():
    mock_open = mock.mock_open(read_data="hi hello")
    expected_result = ["hi hello"]
    with mock.patch("src.file_utils.open", mock_open):
        actual_result = file_utils.get_file_text("text1.txt")
    
        assert expected_result == actual_result
    
def test_append_user_to_list():
    with mock.patch("builtins.open", mock.mock_open()) as mocked_open:
        actual_result = file_utils.append_user_to_list("testuser", "2","test1.txt")

        mocked_open.assert_called_once_with("test1.txt", "a")
        handle = mocked_open()
        handle.write.assert_called_once_with("2: testuser")

