from req import get_page


def check_list_url(input_url):
    try:
        pg = get_page(input_url, time_out=3)
    except:
        pg = None

    if pg == None:
        return None

    if not pg.ok:
        return None

    return pg.url


def get_list_url(url):
    if url == None:
        return None

    url_splitted = url.split('/')

    if len(url_splitted) < 5:
        return None

    if url_splitted[0].startswith('http'):
        https = 'https://'
    else:
        return None

    if url_splitted[1] == '':
        del url_splitted[1]

    if url_splitted[1] == 'www':
        del url_splitted[1]

    if url_splitted[1].startswith('letterboxd'):
        letterboxd = 'letterboxd.com/'
    else:
        return None

    user_name = url_splitted[2] + '/'
    list_name = 'list/' + url_splitted[4] + '/'

    return https + letterboxd + user_name + list_name


def get_page_url(url, i): return url + 'page/' + str(i)


def get_film_url(film_link): return 'https://letterboxd.com' + film_link
