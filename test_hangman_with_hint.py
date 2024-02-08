from hangman_with_hint import match_with_gaps

def test_match_with_gaps():
    assert match_with_gaps('a_ _ le', 'apple')
    assert match_with_gaps('_ _ _ le', 'apple')
    assert match_with_gaps('a_ _ _e', 'apple')
    assert match_with_gaps('a_ _ l_', 'apple')
    assert match_with_gaps('_ _ _l_', 'apple')