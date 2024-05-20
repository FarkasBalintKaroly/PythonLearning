from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template(template_name_or_list="index.html", num=random_number, current_year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
