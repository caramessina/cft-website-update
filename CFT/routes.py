from flask import render_template, flash, redirect, url_for, request, request, jsonify
from CFT import app, db, bcrypt
#importing from files within this package
from CFT.models import User
from CFT.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/blogposts/agency_and_power")
def cf_agency_power():
    return render_template('blogposts/agency_and_power.html', title='Power and Agency')

@app.route("/blogposts/missandei_deserves_better")
def bp_missandei():
    return render_template('blogposts/missandei.html', title='Snippet - Missandei Deserves Better')

@app.route("/blogposts/")
def bp_home():
    return render_template('blogposts/home.html', title='Critical Fan Snippets')

@app.route("/fandom_by_numbers/")
def ffd_numbers():
    return render_template('/fandom_by_numbers/home.html', title='Fandom by Numbers')

@app.route("/fandom_by_numbers/analysis")
def ffd_numbers_analysis():
    return render_template('fandom_by_numbers/analysis.html', title='Fandom by Numbers - Analysis')

@app.route("/fandom_by_numbers/got")
def ffd_numbers_got():
    return render_template('fandom_by_numbers/GOT.html', title='Fandom by Numbers - Game of Thrones')

@app.route("/fandom_by_numbers/tlok")
def ffd_numbers_tlok():
    return render_template('fandom_by_numbers/tlok.html', title='Fandom by Numbers - The Legend of Korra')

@app.route("/fandom_by_numbers/genre_conventions")
def ffd_genre():
    return render_template('fanfic_data/genre_conventions.html', title='Genre Conventions in Fanfic')

@app.route("/fandom_by_numbers/tagging_practices")
def ffd_tagging_practices():
    return  render_template('fanfic_data/tagging_practices.html', title='Tagging Communities')

@app.route("/teaching")
def teaching():
    return  render_template('teaching/home.html', title='Critical Fan Pedagogy')

@app.route("/teaching/about_cfp")
def about_cfp():
    return  render_template('teaching/about_cfp.html', title='About Critical Fan Pedagogy')

@app.route("/teaching/cfp_resources_instructors")
def cfp_resources_instructors():
    return  render_template('teaching/cfp_resources_instructors.html', title='Critical Fan Pedagogy Resources for Instructors')

@app.route("/teaching/resources/Critical_Fan_Research_Methods_Syllabus")
def cfp_syllabus01():
    return  render_template('teaching/resources/cfp_syllabus.html', title='Critical Fan Research Methods Syllabus')

@app.route("/about_dissertation/acknowledgements")
def dis_acknowledgements():
    return  render_template('/about_dissertation/acknowledgements.html', title='Dissertation Acknowledgements')

@app.route("/about_dissertation/cara_marta_messina")
def dis_about_cara():
    return  render_template('/about_dissertation/cara_marta_messina.html', title='About Cara Marta Messina')

@app.route("/about_dissertation/computational_essays")
def dis_computational_essays():
    return  render_template('/about_dissertation/computational-essays.html', title='Computational Essays')

@app.route("/about_dissertation/framework")
def dis_framework():
    return  render_template('/about_dissertation/framework.html', title='Dissertation Framework')

@app.route("/about_dissertation/literature_review")
def dis_lit_review():
    return  render_template('/about_dissertation/literature_review.html', title='Dissertation Litearture Review')

@app.route("/about_dissertation/methods")
def dis_methods():
    return  render_template('/about_dissertation/methods.html', title='Dissertation Methods')

@app.route("/bibliography")
def bibliography():
    return  render_template('/bibliography.html', title='Bilbiography')

@app.route('/interviews')
def interviews():
    return render_template('interviews/home.html', tite='Interviews')

@app.route('/interviews/qualitative_coding')
def interviews_qualitative_coding():
    return render_template('interviews/qualitative_coding.html', tite='Qualitative Coding Description')

@app.route("/interviews/search", methods=['GET', 'POST'])
def interview_search():
    return render_template('/interviews/search.html', title='Search Interviews')

@app.route('/interviews/writegirl')
def interview_wg():
    return render_template('interviews/writegirl-interview-transcription.html', tite='Interview - Writegirl')

@app.route('/interviews/dialux')
def interview_dia():
    return render_template('interviews/dialux-interview-transcription.html', tite='Interview -Dialux ')

@app.route('/interviews/gillywulf')
def interview_gw():
    return render_template('interviews/gillywulf-interview-transcription.html', tite='Interview - Gillywulf')

@app.route('/interviews/kittya')
def interview_kittya():
    return render_template('interviews/kittya-interview-transcription.html', tite='Interview - Kittya')

@app.route('/interviews/valk')
def interview_valk():
    return render_template('interviews/valk-interview-transcription.html', tite='Interview - Valk')

@app.route('/interviews/aria')
def interview_aria():
    return render_template('interviews/aria-interview-transcription.html', tite='Interview - Aria')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title='User Dashboard')
