from flask import Flask, render_template, request
import requests
import smtplib
import os

posts_url = "https://api.npoint.io/674f5423f73deab1e9a7"

all_posts = requests.get(url=posts_url).json()

app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template(template_name_or_list="index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template(template_name_or_list="about.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in all_posts:
        if post["id"] == index:
            requested_post = post
    return render_template(template_name_or_list="post.html", post=requested_post)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        form_message = request.form["message"]
        my_email = os.environ.get("MY_EMAIL")
        password = os.environ.get("MY_EMAIL_PASSWORD")
        to_email = os.environ.get("MY_EMAIL")
        message = f"Subject:New message from Blog\n\n" \
                  f"Name: {name}\n" \
                  f"E-mail: {email}\n" \
                  f"Phone: {phone}\n" \
                  f"Message: {form_message}"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)

        title_message = "Successfully sent your message!"
        return render_template(template_name_or_list="contact.html", title=title_message)
    title_message = "Contact Me"
    return render_template(template_name_or_list="contact.html", title=title_message)


if __name__ == "__main__":
    app.run(debug=True)
