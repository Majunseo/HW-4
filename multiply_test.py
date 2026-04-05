from multiply import times
def test_times():
    assert times([2, 3]) == 6
    assert times([-1, 1]) == -1
    assert times([0, 0]) == 0
    
    assert times([2, 3, 1]) == 6
    assert times([-1, 1, 1]) == -1
    assert times([0, 0, 0]) == 0
test_times()