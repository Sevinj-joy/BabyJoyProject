from run import app
from flask import render_template


@app.route("/admin", )
def app_admin():
    return render_template("admin/Admin_panel.html")


@app.route("/admin_edit")
def app_admin_edit_page():
    return render_template("admin/Edit_products.html")

    