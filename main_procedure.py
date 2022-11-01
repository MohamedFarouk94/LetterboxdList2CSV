from req import get_page
from lbxd import extract_list, extract_film, extract_dyr
from url import check_list_url, get_list_url, get_page_url, get_film_url
from film import Film, to_csv
from tqdm import tqdm

EXTERNAL_INTERRUPT = False
LOADING = 0


def set_interrupt():
    global EXTERNAL_INTERRUPT
    EXTERNAL_INTERRUPT = True


def clear_interrupt():
    global EXTERNAL_INTERRUPT
    EXTERNAL_INTERRUPT = False


def clear_loading():
    global LOADING
    LOADING = 0


def read_loading():
    global LOADING
    return LOADING


def handle_url(input_url):
    url = get_list_url(check_list_url(input_url))
    return url


def create_list(url):
    page_i = 1
    list_of_films = []
    while True:
        pg = get_page(get_page_url(url, page_i))
        films_codes = extract_list(pg)
        for film_code in films_codes:
            index = len(list_of_films) + 1
            film_title, film_link = extract_film(film_code)
            list_of_films.append(Film(ind=index, title=film_title, link=film_link))

        if len(films_codes) == 100:
            page_i += 1
        else:
            break

    return list_of_films


def complete_list(list_of_films, verbose=1):
    global EXTERNAL_INTERRUPT, LOADING
    iterable_object = tqdm(list_of_films) if verbose else list_of_films
    n_films = len(list_of_films)
    for i, film in enumerate(iterable_object):
        if EXTERNAL_INTERRUPT:
            return None
        pg = get_page(get_film_url(film.link), time_out=20)
        try:
            film.director, film.year, film.rating = extract_dyr(pg)
        except:
            print(f'An error happened in film: {film.link}')
            return
        LOADING = (i+1) / n_films
    return list_of_films if len(list_of_films) else None


def quick_run(input_url, verbose=1):
    url = handle_url(input_url)
    list_of_films = create_list(url)
    list_of_films = complete_list(list_of_films, verbose=verbose)

    if (list_of_films):
        return list_of_films

    print("SOMETHING WRONG")
    return
