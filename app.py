from flask import Flask, Blueprint, render_template
from Main_Page_Folder.main_page_app import main_page

app = Flask(__name__)
app.register_blueprint(main_page)


if __name__ == "__main__":
    app.run(debug=True)
