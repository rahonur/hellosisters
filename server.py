from flask import (Flask, render_template, request, flash, session,
                   redirect)
from flask_login import LoginManager, login_user, login_user, logout_user, login_required, current_user
from model import connect_to_db, User, Blog
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

######################################################################################
#Roroadmin 
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def load_user(user_id):
    return User.get(user_id)
######################################################################################
#route for homepage 

@app.route('/')
def index():
    """Show the homepage"""

    if 'username' in session:
        username = session['username']
        User = User.query.filter_by(username=username).first_or_404()

        blogs = Blog.query.all()

        # blogentries = BlogEntrie.query.all()

        # blogcomments = BlogComment.query.all()

        return render_template("profile.html", user=user,blogs = blogs, 
        users=users, username=username)

    else:
        return render_template('index.html')
    return render_template('base.html')


######################################################################################
#User Login and authentication

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form["username"]
    password = request.form["password"]

    check_user = User.query.filter_by(username = username).first()

    if check_user.password == password:
        login_user(check_user)
        return redirect(f"/profile/{check_user.user_id}")
    else:
        flash("Incorrect username and/or password. Please try again.")
        return redirect("/login")
######################################################################################

#User Signup 

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    if request.method == "POST":

        db.session.add(new_user)
        db.session.commit()

        user_id = new_user.user_id
        session["user_id"] = user_id

        flash("New User profile created!")
        return redirect(f"/profile/{user_id}")
    else:
        return redirect(f"/")

################################################################################
@app.route('/profile/<int:user_id>')
def userprofile(user_id):
    """This is the user's homepage."""
    
    user = User.query.get(user_id)
#    for activity in parent.activities:
#        activity.matches = Activity.query.get(activity.activity_id).parents



    #children = Child.query.filter(Child.parents.parent_id==parent_id).all()
    #activities = Activity.query.filter(Activity.parents.parent_id==parent_id).all()

    return render_template("profile.html",
                           #children=children,
                           #activities=activities,
                           parent=parent)
################################################################################




# Logout
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect ('/')

# @app.route('/')
# def homepage():
#     """View homepage."""

#     return render_template('base.html')

# @app.route('/about')
# def get_about_page():
#     """View About page."""

#return render_template('about.html')

# @app.route('/main-menu')
# def show_main_menu():
#     """Go to references page"""

#     return render_template('main-menu.html')

@app.route('/add-user')
def add_user():
    """View add user page"""

    return render_template('register-form.html')

@app.route('/signin')
def signin():
    """View login page"""
    user_id = session.get("user_id")
    if user_id:
        flash(user_id)

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():
    """Log a user into the website"""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.check_user_login_info(email, password)

    if user:
        session["user_id"] = user.user_id
        return redirect('/directory')

    else:
        flash('Login info is incorrect, try again.')
        return redirect('/signin')

# @app.route('/profile')
# def profile():

#     """display user's profile page"""
if __name__ == '__main__':
    connect_to_db(app)
    app.run(port=5000, host='0.0.0.0', debug=True)