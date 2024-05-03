import csv

import click

from . import app, db
from .models import Review


@app.cli.command('load_reviews')
def load_reviews_command():
    """The function for uploading reviews to the database."""
    with open('reviews.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        counter = 0
        for row in reader:
            review = Review(**row)
            db.session.add(review)
            db.session.commit()
            counter += 1
    click.echo(f'Loaded reviews: {counter}')
