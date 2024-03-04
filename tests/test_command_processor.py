import pytest
from utils.translation import translation_helper as helper


@pytest.mark.parametrize(
    "text, output",
    [
        ("", ""),
        (" ", ""),
        ("      ", ""),
        ("\n", ""),
        ("\r\n\t\v\f ", ""),
        ("Apple mango", "Apple mango"),
        ("\nApple mango ", "Apple mango"),
        ("Apple   mango", "Apple mango"),
        ("Apple \r\n\t\v\f mango", "Apple\nmango"),
        ("Apple\nmango", "Apple\nmango"),
        ("Apple\n\nmango", "Apple\nmango"),
        ("Apple \n \n mango", "Apple\nmango"),
        ("Apple \n \r\n\t\v\f \n mango", "Apple\nmango"),
    ],
)
def test_sanitize(text, output):
    assert helper.sanitize(text) == output
