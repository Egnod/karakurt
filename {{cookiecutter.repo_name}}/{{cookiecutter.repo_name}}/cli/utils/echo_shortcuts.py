from art import text2art

from {{cookiecutter.repo_name}} import metadata


def get_art_title():
    title = text2art(metadata.name, font="alligator2", chr_ignore=True)

    return f"{title}"
