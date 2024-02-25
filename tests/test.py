from mypackage import mymodule
def test_topn():
    '''making sure tha topn works correctly'''


    assert mymodule.topn([5, 3, 8, 1, 9, 2, 7, 4, 6], 3) ==  [9, 8, 7], 'incorrect'
    assert mymodule.topn(['apple', 'banana', 'orange', 'grape'], 2) == ['orange', 'grape'], 'incorrect'
    assert mymodule.topn([1,2,3,4,5,6], 2) == [6,5], 'incorrect'
