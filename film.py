import pandas as pd
import os


class Film:
    def __init__(self, ind=0, title='', link='', year=1800, director='', rating=4.99):
        self.ind = ind
        self.title = title
        self.link = link
        self.year = year
        self.director = director
        self.rating = rating


    def __str__(self):
        return f'{self.ind}. {self.title} ({self.year}), {self.director} [{self.rating}]'


    def __repr__(self):
        return f'{self.ind}. {self.title} ({self.year}), {self.director} [{self.rating}]'



def to_df(list_of_films):
    df_of_films = {
        'Ind': [film.ind for film in list_of_films],
        'Title': [film.title for film in list_of_films],
        'Year': [film.year for film in list_of_films],
        'Director': [film.director for film in list_of_films],
        'Rating': [film.rating for film in list_of_films]}

    return pd.DataFrame(df_of_films)


def to_csv(list_of_films, path, file_name='letterboxd_list'):
    df = to_df(list_of_films)
    if file_name+'.csv' in os.listdir(path):
        for i in range(1234567):
            new_file_name = f'{file_name}({i+1})'
            if new_file_name+'.csv' in os.listdir(path):
                continue
            file_name = new_file_name
            break
    df.to_csv(os.path.join(path,file_name+'.csv'), index=False)
    return True
