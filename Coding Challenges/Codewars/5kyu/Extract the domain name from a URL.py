# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

def domain_name(url):
    for _ in ['http://www.', 'https://www.', 'http://', 'https://', 'www.', '']:
        if _ in url:
            return url[len(_):url.index('.', len(_))]
