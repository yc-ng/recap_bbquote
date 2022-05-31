from bbquote.lib import get_quote

def test_quote_data_type():
    quote, author = get_quote()
    assert type(quote) == str
    assert type(author) == str
