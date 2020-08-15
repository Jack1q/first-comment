from flask import Flask, render_template
from firstcomment import FirstComment

app = Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return render_template('first.html')

@app.route('/<string:id>')
def get_comment(id):
    f = FirstComment()
    comment_data = f.get_last_comment(f.youtube, id)
    return render_template(
        'index.html', 
        text=comment_data['text'],
        name=comment_data['name'],
        photo_url=comment_data['photo_url'],
        date=comment_data['date']
    )

if __name__ == '__main__':
    app.run(debug=True)