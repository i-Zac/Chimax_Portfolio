from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def home ():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_pages (page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {name}, {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar=';', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            name = data.get("name", "Guest")
            write_to_csv(data)
            return redirect(url_for('thank_you', name=name))
        except:
            return 'Did not save to database'
    else:
        return 'something went wrong! Try again!'

@app.route('/thank_you')
def thank_you():
    name = request.args.get('name', 'Guest')
    return render_template('thank_you.html', name=name)



if __name__ == '__main__':
    app.run (debug = True)