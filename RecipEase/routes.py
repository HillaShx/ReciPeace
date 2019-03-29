from flask import render_template, url_for, flash, redirect, Markup
from RecipEase import app
from RecipEase.forms import RegistrationForm, LoginForm
from RecipEase.mysql_operations import insert,read
# import mysql.connector
from RecipEase import recipe_db


cur = recipe_db.cursor()

recipe_list = [
    {
    'Name' : 'Pork Chop Skillet',
    'Ingredients' : '2 tablespoons butter\n4 boneless pork chops\n1 1/4 cups water\n1 (6 ounce) package long grain and wild rice mix with herbs\n1 (15.25 ounce) can corn, undrained\n1 (14.5 ounce) can diced Italian-style tomatoes, undrained',
    'Instructions' : 'Heat butter in a skillet over medium heat; cook pork chops in the melted butter until cooked through, 10 to 15 minutes. Remove pork chops from skillet and cut into bite-sized pieces.\nPour water and long grain and wild rice mix with herbs into the same skillet; stir well. Layer pork chop pieces over rice. Pour corn over pork chops layer; top with tomatoes. Cover skillet and simmer until rice is tender and liquid is absorbed, 30 to 40 minutes.',
    'Total_Time' : '55 m',
    'Serving' : '4',
    'Img_Name' : '3721817',
    'Rating' : '4.55556'
    },
    {
    'Name' : 'Overnight Chai Oatmeal',
    'Ingredients' : '1 cup oats\n1 cup almond-coconut milk\n2 tablespoons chia seeds\n2 tablespoons shredded coconut\n1/4 teaspoon ground cardamom\n1/4 teaspoon ground cinnamon\n1/4 teaspoon vanilla extract\n1/4 teaspoon ground ginger\n1/4 teaspoon nutmeg',
    'Instructions' : 'Combine oats, almond-coconut milk, chia seeds, coconut, cardamom, cinnamon, vanilla extract, ginger, and nutmeg in a bowl. Cover bowl with plastic wrap and refrigerate, 8 hours to overnight.',
    'Total_Time' : '8 h 10 m',
    'Serving' : '2',
    'Img_Name' : '1122507',
    'Rating' : '3.96429'
    }
]


@app.route("/")
@app.route("/home")
def homepage():
    return render_template('homepage.html')

@app.route("/about")
def about():
    return render_template('recipes.html', recipe_list=recipe_list, title="Recipes")

@app.route("/recipes")
def recipes():
    return render_template('recipes.html', recipe_list=recipe_list, title="Recipes")

# cur.execute("CREATE TABLE recipes (ID INTEGER AUTO_INCREMENT PRIMARY KEY, Ingredients VARCHAR(1000), Instructions TEXT, Total_Time VARCHAR(7), Servings TINYINT(2), Img_Name INT, Rating FLOAT);")
# cur.execute("ALTER TABLE recipes ADD Name VARCHAR(100);")
# cur.execute("ALTER TABLE recipes CHANGE COLUMN Name Name varchar(100) AFTER ID;")
# insert_command = "DROP TABLE recipes;"
# cur.execute(insert_command)
# insert_command = "INSERT INTO restrictions (Ingredient, Restriction_Type) VALUES (%s,%s);"

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.validate_username(form.username.data) and form.validate_email(form.email.data):
            # print("register:",type(form.username.data))
            flash(f'Account created for {form.username.data}! You are now able to log in!', 'success')
            insert(form.username.data,form.email.data,form.password.data,form.pic_filename)
            return redirect(url_for('login'))
        elif not form.validate_username(form.username.data):
            flash(f'There is already an account using this username. Please choose a different one.', 'danger')
        elif not form.validate_email(form.email.data):
            flash(Markup(f'<div class="alert-danger">There is already an account using this email address. <a href="{{ url_for("forgot_password.html") }}"  class="flash-link">Forgot your password?</a></div>'))
    return render_template('register.html', form=form, title="Register")

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        is_valid = form.validate_login_info(form.email.data,form.password.data)[0]
        if is_valid:
            curr_username = form.validate_login_info(form.email.data,form.password.data)[1]
            # print(password_is_valid)
            # print(curr_username)
            # if form.validate_email_login(form.email.data) and password_is_valid:
            flash(f'You are now logged in! Welcome, {curr_username}!', 'success')
            return redirect(url_for('homepage'))
        else:
            flash(f'Login unsuccessful! Please check your email and password.', 'danger')
    return render_template('login.html', form=form, title="Login")
