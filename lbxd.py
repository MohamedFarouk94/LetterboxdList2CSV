def extract_list(page):
    try:
        pg_content = page.content.decode('utf8')
    except AttributeError:
        return []

    start_list = '<ul class="js-list-entries poster-list -p125 -grid film-list">'
    end_list = '</ul>'
    sep_list = '</li>'
    try:
        the_list_and_beyond = pg_content.split(start_list)[1]
        the_list = the_list_and_beyond.split(end_list)[0]
        films_codes = the_list.split(sep_list)
        del films_codes[-1]
        return films_codes
    except:
        return []


def extract_film(film_code):
    film_title = film_code.split('alt="')[1].split('"/> <span class=')[0]
    film_link = film_code.split(
        'data-target-link="')[1].split('" data-target-link-target=""')[0]
    return film_title, film_link


def extract_director(page):
    pg_content = page.content.decode('utf8')
    pre_director = 'Directed by" /><meta name="twitter:data1" content="'
    post_director = '" />\n\t<meta name="twitter:label2" content="Average'
    director_and_beyond = pg_content.split(pre_director)[1]
    director = director_and_beyond.split(post_director)[0]
    return director


def extract_year(page):
    pg_content = page.content.decode('utf8')
    post_year = ')" />\n\t<meta property="og:description" content="'
    year = pg_content.split(post_year)[0][-4:]
    try:
        return int(year)
    except:
        return 1800


def extract_rating(page):
    pg_content = page.content.decode('utf8')
    before_rating = '"ratingValue":'
    rating = pg_content.split(before_rating)[1][:4]
    rating = rating.split(',')[0]
    return float(rating)


def extract_dyr(page):
    pg_content = page.content.decode('utf8')

    post_year = ')" />\n\t<meta property="og:description" content="'
    pre_director = 'Directed by" /><meta name="twitter:data1" content="'
    post_director = '" />\n\t<meta name="twitter:label2" content="Average'
    before_rating = '"ratingValue":'

    year = pg_content.split(post_year)[0][-4:]

    try:
        year = int(year)
    except:
        year = 1800

    director_and_beyond = pg_content.split(pre_director)[1]
    director = director_and_beyond.split(post_director)[0]

    rating = pg_content.split(before_rating)[1][:4]
    rating = rating.split(',')[0]
    rating = float(rating)

    return director, year, rating
