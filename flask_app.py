from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    # verify that the name has at least 4 characters
    # verify that the first letter of the name is uppercase

    dropdown = request.form.get('input_dropdown', '')
    # if the dropdown value is red fish, show a red fish picture
    # if it is instead blue fish, then show a blue fish picture

    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    return render_template("main_page.html", input_data=dropdown,
                           output="You're a wizard %s." % name)

def dedupe(x):
    y = []
    for i in x:
        if i not in x:
            y.append(i)
    return y

animals = ['cats', 'cats', 'cats', 'dogs', 'pandas']
print(dedupe(animals)) # prints ['cats', 'dogs', 'pandas']



