from logging import info, debug
from .generate_file import generate_path
from .generate_author_id_year import get_author_id_year


def save_csv_file(response, token, organism):
    # method responsable for save csv file
    # and getting token
    # and mount directory`s name pattern
    # :param str token: collection`s identification

    # filename variable receive URL collection page
    # splitted by slash, question mark and equals
    # to get filename from URL
    filename = response.url.split('/')[-1].split('?')[-1].split('=')[-1]

    # split token to get separated year, name and identification
    author, ID, year = get_author_id_year(token.split('-'))

    # path variable receive generated path to save file
    path = generate_path(filename, ID, author, year, organism)

    # info point
    # info(f'Saving on {path}')

    # open created file to write data
    with open(path, 'wb') as f:

        # write csv data on file
        f.write(response.body)