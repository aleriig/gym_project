from flask import Flask, render_template

from controllers.sport_classes_controller import sport_classes_blueprint
from controllers.members_controller import members_blueprint
from controllers.booking_lists_controller import booking_lists_blueprint


app = Flask(__name__)

app.register_blueprint(booking_lists_blueprint)
app.register_blueprint(sport_classes_blueprint)
app.register_blueprint(members_blueprint)


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
