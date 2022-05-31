from bbquote.lib import get_quote

def test_quote_data_type():
    assert type(get_quote()) == str
