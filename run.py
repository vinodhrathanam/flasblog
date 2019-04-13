
from flaskblog import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True,host='10.48.19.200')
