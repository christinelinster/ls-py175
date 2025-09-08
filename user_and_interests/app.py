from flask import Flask, render_template, redirect
import yaml

app = Flask(__name__)
with open("users.yaml", "r") as file:
        users = yaml.safe_load(file)

def total_interests(users):
     return sum(len(user['interests']) for user in users.values())

@app.route('/')
def home():
    return redirect("/users")

@app.route('/users')
def users_list():
    return render_template('users.html', 
                           users=users,
                           total_users=len(users),
                           total_interests=total_interests(users)
                           )

@app.route('/users/<username>')
def user_profile(username):
    user = users.get(username)
    return render_template('user.html', 
                           username=username, 
                           user=user,
                           users=users,
                           total_users=len(users),
                           total_interests=total_interests(users)
                           )

if __name__ == '__main__':
    app.run(debug=True, port=5003)