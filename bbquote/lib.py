import requests

def get_quote():

    url = 'https://wagon-breaking-bad-quotes.herokuapp.com/v1/quotes'

    response = requests.get(url).json()
    if len(response)==0:
        return None

    quote = f"\"{response[0]['quote']}\" \n- {response[0]['author']}"
    return quote

if __name__ == '__main__':
    print(get_quote())
