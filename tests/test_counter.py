from lib.counter import Counter

# tests counter when only add one number
def test_counter_right_single():
    counter = Counter()
    counter.add(33)
    result = counter.report()
    assert result == "Counted to 33 so far."

#tests counter when we add multiple numbers
def test_counter_right_multiple():
    counter = Counter()
    counter.add(33)
    counter.add(45)
    result = counter.report()
    assert result == "Counted to 78 so far."

