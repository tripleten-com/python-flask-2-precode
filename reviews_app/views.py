from random import randrange

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import ReviewForm
from .models import Review


@app.route('/')
def index_view():
    quantity = Review.query.count()
    if not quantity:
        abort(404)
    offset_value = randrange(quantity)
    review = Review.query.offset(offset_value).first()
    return render_template('review.html', review=review)


@app.route('/add', methods=['GET', 'POST'])
def add_review_view():
    form = ReviewForm()
    if form.validate_on_submit():
        text = form.text.data
        if Review.query.filter_by(text=text).first() is not None:
            flash('This review already exists!')
            return render_template('add_review.html', form=form)
        review = Review(
            title=form.title.data,
            text=form.text.data,
            source=form.source.data
        )
        db.session.add(review)
        db.session.commit()
        return redirect(url_for('review_view', id=review.id))
    return render_template('add_review.html', form=form)


@app.route('/reviews/<int:id>')
def review_view(id):
    review = Review.query.get_or_404(id)
    return render_template('review.html', review=review)
