from hangman_with_hint import match_with_gaps

def test_match_with_gaps():
    assert match_with_gaps('a_ _ le', 'apple')
    assert match_with_gaps('_ _ _ le', 'apple')
    assert match_with_gaps('a_ _ _e', 'apple')
    assert match_with_gaps('a_ _ l_', 'apple')
    assert match_with_gaps('_ _ _l_', 'apple')

def test_match_with_gaps_wrong_length():
    assert not match_with_gaps('a _ le', 'apple')
    assert not match_with_gaps('d_ og', 'dog')
    assert not match_with_gaps('su_', 'sunny')
    assert not match_with_gaps('_able', 'able')
    assert not match_with_gaps('t_ _ e', 'tan')

def test_match_with_gaps_double_letters():
    assert not match_with_gaps('a _ ple', 'apple')
    assert not match_with_gaps('su_ _ e_s', 'success')
    assert match_with_gaps('su _ _ ess', 'success')
    assert not match_with_gaps('g_ _ l', 'gull')
    assert match_with_gaps('g _ ll', 'gull')
