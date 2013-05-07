from urllib import parse

def clean_url(url):
    if url.startswith("http://"):
        url = url[7:len(url)]
    elif url.startswith("https://"):
        url = url[8:len(url)]

    # Replace unsafe characters
    url = parse.quote(url)

    return url  

