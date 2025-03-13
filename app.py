from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    success = False
    name = ""
    if request.method == 'POST':
        name = request.form.get('name')
        success = True
    return render_template("contact.html", success=success, name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
