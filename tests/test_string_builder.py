from lib.string_builder import StringBuilder
#tests when we only add one string
def test_string_builder_single():
    stringbuilder = StringBuilder()
    stringbuilder.add("This is a string")
    result = stringbuilder.size()
    assert result == 16
    result = stringbuilder.output()
    assert result == "This is a string"

def test_string_builder_multiple():
    stringbuilder = StringBuilder()
    stringbuilder.add("This is a string. ")
    stringbuilder.add("This is also a string.")
    result = stringbuilder.size()
    assert result == 40
    result = stringbuilder.output()
    assert result == "This is a string. This is also a string."


