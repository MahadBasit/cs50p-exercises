from twttr import shorten

def test_shorten():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('MaHad') == 'MHd'
    assert shorten('tw1TT5r') == 'tw1TT5r'
    assert shorten('aeiou') == ''
    assert shorten('') == ''