from WebSite import create_app
from WebSite import create_database
from WebSite import create_database
from WebSite import models
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

