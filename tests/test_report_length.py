from lib.report_length import report_length

def test_report_length_correct():
    result = report_length("Hello, this string is 24")
    assert result == "This string was 24 characters long."