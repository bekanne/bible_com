#!/usr/bin/env python3

import argparse
import configparser
import webbrowser
import sys
import os


def read_config():
    """Read the config file and return the config object."""
    # Get the directory of the current script file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config.cfg')
    # Read the configured language
    language_config = configparser.ConfigParser(allow_no_value=True)
    language_config.read(config_path)
    language = list(language_config['language'].keys())[0]
    config_path = os.path.join(script_dir, f'config_{language}.cfg')
    config = configparser.ConfigParser()
    config.read(config_path)
    return config


def get_book_name(book):
    """Return the book name from the config file and the given book variable.
    Allow the book variable to be similar or incomplete to the book names from the config file."""
    # Read the list of books from the config file
    config = read_config()
    books = config.options('books')
    # Check if the given book variable is similar or incomplete to the book names from the config file
    for book_name in books:
        if book_name.lower().startswith(book.lower()):
            return book_name
    # If the given book variable is not similar or incomplete to the book names from the config file, return the given book variable
    return book


def get_book(book):
    """Return the book shortcut from the config file and the given book variable."""
    # Read the list of books from the config file
    config = read_config()
    book = get_book_name(book)
    try:
        book_shortcut = config.get('books', book)
    except ValueError:
        print('Invalid book name.')
        print(f'Config: {config}')
        exit(1)
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        print(f'Error by reading config: {e}')
        exit(1)
    return book_shortcut


def get_translation(translation):
    """Return the translation id from the config file and the given translation variable."""
    # Read the list of translations from the config file
    section_name = 'translations'
    config = read_config()
    if translation == 'None':
        translation_id = config.get(section_name, config.options(section_name)[0])
        return translation_id
    else:
        try:
            translation_id = config.get(section_name, translation)
        except (ValueError, configparser.NoOptionError):
            print('Invalid translation name. Using default.')
            return 157
        return translation_id


def create_parser() -> argparse.ArgumentParser:
    """Create an argument parser."""
    parser = argparse.ArgumentParser(description='Open Bible verses in web browser.')

    # Define the command line arguments
    parser.add_argument('book', help='Name of the book - can be upper or lower case, also just the beginning of the book name (e.g. \'heb\' for Hebrews)')
    parser.add_argument('chapter', type=int, help='Chapter number')
    parser.add_argument('verse', nargs='?', type=int, help='Verse number')
    parser.add_argument('-t', '--translation', type=str, help='Translation version')
    parser.add_argument('-p', '--parallel', type=str, help='Translation for parallel view')

    return parser


def construct_url(book, chapter, verse=None, translation=None, parallel=None):
    """Construct the URL for the given book, chapter, and verse."""
    # Get the index of the book in the list of books

    book_shortcut = get_book(book)
    if not translation:
        translation_id = get_translation('None')
    else:
        translation_id = get_translation(translation)

    if parallel:
        parallel_translation_id = get_translation(parallel)

    # Construct the URL
    url = f'https://www.bible.com/bible/{translation_id}/{book_shortcut}.{chapter}'
    if verse:
        url += f'.{verse}'
    if parallel:
        url += f'?parallel={parallel_translation_id}'
    return url


def open_url(url):
    """Open the given URL in a web browser."""
    webbrowser.open(url)


def main():
    # Create an argument parser
    parser = create_parser()

    if len(sys.argv) == 1:
        print(parser.format_help())
        sys.exit(1)

    # Parse the command line arguments
    args = parser.parse_args()

    # Construct the URL
    url = construct_url(args.book, args.chapter, args.verse, args.translation, args.parallel)

    # Open the URL in a web browser
    open_url(url)


if __name__ == '__main__':
    main()
