from flask import Flask, Blueprint, render_template
from Home_Page_Folder.home_page_app import home_page

app = Flask(__name__)
app.register_blueprint(home_page)


if __name__ == "__main__":
    app.run(debug=True)
