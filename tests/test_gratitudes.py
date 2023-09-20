from lib.gratitudes import Gratitudes
#tests for one grat added
def test_gratitudes_single():
    gratitudes = Gratitudes()
    gratitudes.add("Friendship")
    result = gratitudes.format()
    assert result == "Be grateful for: Friendship"


#tests for multiple grat added
def test_gratitudes_multiple():
    gratitudes = Gratitudes()
    gratitudes.add("Friendship")
    gratitudes.add("Family")
    result = gratitudes.format()
    assert result == "Be grateful for: Friendship, Family"