from flask import render_template, flash, redirect, url_for, request, request, jsonify
from CFT import app, db, bcrypt
#importing from files within this package
from CFT.models import User, WebText
from CFT.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/homepath_teacher")
def homepath_teacher():
    return  render_template('teaching/home.html', title='Critical Fan Pedagogy')

@app.route("/homepath_fan")
def homepath_fan():
    return  render_template('homepath_fan.html', title='Path - Fan Users')

@app.route("/homepath_scholar")
def homepath_scholar():
    return  render_template('homepath_scholar.html', title='Path - Scholar Users')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/cite")
def cite():
    return render_template('cite.html', title='How to Cite the Critical Fan Toolkit')

##############CASE STUDIES################
@app.route("/case_studies/korrasami_canon")
def bp_korrasami():
    return render_template('case_studies/korrasami_canon.html', title='Power and Agency')

@app.route("/case_studies/missandei_deserves_better")
def bp_missandei():
    return render_template('case_studies/missandei.html', title='Snippet - Missandei Deserves Better')

@app.route("/case_studies/")
def bp_home():
    return render_template('case_studies/home.html', title='Critical Fan Snippets')

##############FANDOM BY NUMBERS################
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

##############TEACHING RESOURCES################
@app.route("/teaching")
def teaching():
    return  render_template('teaching/home.html', title='Critical Fan Pedagogy')

@app.route("/homepath_teaching")
def homepath_teaching():
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

@app.route("/teaching/resources/assignment-restoring-for-justice")
def cfp_assignment_justice():
    return  render_template('teaching/resources/assignment-restorying-for-justice.html', title='Assignment - Restorying for Justice')

@app.route("/teaching/resources/research-project")
def cfp_assignment_research():
    return  render_template('teaching/resources/research_project.html', title='Assignment - Restorying for Justice')

@app.route("/teaching/resources/activity-fandom-statistics")
def cfp_activity_fanstats():
    return  render_template('teaching/resources/activity-fandom-statistics.html', title='Activity - Fandom Statistics')

##############ABOUT DISSERTATION################

@app.route("/about_dissertation/")
def dis_home():
    return  render_template('/about_dissertation/home.html', title='About this Dissertation')

@app.route("/about_dissertation/abstract")
def dis_abstract():
    return  render_template('/about_dissertation/abstract.html', title='Dissertation Abstract')

@app.route("/about_dissertation/acknowledgements")
def dis_acknowledgements():
    return  render_template('/about_dissertation/acknowledgements.html', title='Dissertation Acknowledgements')

@app.route("/about_dissertation/cara_marta_messina")
def dis_about_cara():
    return  render_template('/about_dissertation/cara_marta_messina.html', title='About Cara Marta Messina')

@app.route("/about_dissertation/implications")
def dis_implications():
    return  render_template('/about_dissertation/implications.html', title='Dissertation Implications')

@app.route("/about_dissertation/research_ethics")
def dis_ethics():
    return  render_template('/about_dissertation/research_ethics.html', title='Research Ethics')

@app.route("/about_dissertation/computational_essays")
def dis_computational_essays():
    return  render_template('/about_dissertation/computational-essays.html', title='Computational Essays')

@app.route("/about_dissertation/computational_essays/data_preparation")
def dis_computational_essays_dataPrep():
    return  render_template('/about_dissertation/computational_essays/data_preparation.html', title='Computational Essay - Data Preparation')

@app.route("/about_dissertation/computational_essays/metadata_analytics")
def dis_computational_essays_metadata():
    return  render_template('/about_dissertation/computational_essays/metadata_analysis.html', title='Computational Essay - Metadata Analytics')

@app.route("/about_dissertation/computational_essays/tag_exploration")
def dis_computational_essays_tagExploration():
    return  render_template('/about_dissertation/computational_essays/tag_exploration.html', title='Computational Essay - Exploring Additional Tags')

@app.route("/about_dissertation/computational_essays/preparing_textual_data")
def dis_computational_essays_textualData():
    return  render_template('/about_dissertation/computational_essays/textual_preparation.html', title='Computational Essay - Preparing Textual Data')

@app.route("/about_dissertation/computational_essays/word_embedding")
def dis_computational_essays_w2v():
    return  render_template('/about_dissertation/computational_essays/w2v.html', title='Computational Essay - Word Embedding Models')

@app.route("/about_dissertation/computational_essays/missandei")
def dis_computational_essays_missandei():
    return  render_template('/about_dissertation/computational_essays/missandei.html', title='Computational Essay - Missandei Deserves Better')

@app.route("/about_dissertation/computational_essays/XML_parser")
def dis_computational_essays_XML():
    return  render_template('/about_dissertation/computational_essays/XML_parser.html', title='Computational Essay - XML Parser')

@app.route("/about_dissertation/computational_essays/network_analysis")
def dis_computational_essays_network():
    return  render_template('/about_dissertation/computational_essays/network_analysis.html', title='Computational Essay - Network Analysis')

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

##############INTERVIEWS#############
@app.route('/interviews')
def interviews():
    return render_template('interviews/home.html', tite='Interviews')

@app.route('/interviews/qualitative_coding')
def interviews_qualitative_coding():
    return render_template('interviews/qualitative_coding.html', tite='Qualitative Coding Description')

@app.route('/interviews/analysis')
def interview_analysis():
    return render_template('interviews/analysis.html', tite='Interviews Analysis')

@app.route('/interviews/vizualization')
def interview_viz():
    return render_template('interviews/viz.html', tite='Interview Vizualization')

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

##############SEARCHES#############
@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        searchTerm = form.searchTerm.data
        results = Results.query.filter("%" + searchTerm + "%").all()
        flash("Here's what we could find", 'success')
        return render_template('results.html', title="Search Results", results=results)
    return render_template('search_form.html', title="Search", form=form)

##########LOGIN INFO##########
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

############### FORGOT PASSWORD ############
