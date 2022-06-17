from flask import Flask, render_template, redirect, url_for
from flask_wtf import Form
from wtforms import SubmitField

app = Flask(__name__)
app.secret_key = 'davidism'

class StatsForm(Form):
    user_stats = SubmitField()
    room_stats = SubmitField()

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    form = StatsForm()

    if form.validate_on_submit():
        if form.user_stats.data:
            return redirect(url_for('user_stats'))
        elif form.room_stats.data:
            return redirect(url_for('room_stats'))

    return render_template('stats.html', form=form)

app.run(debug=True)
