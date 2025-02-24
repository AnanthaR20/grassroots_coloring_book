grassroots_coloring_book = django project head folder
    |- grassroots_coloring_book: root of website, defines interactions between apps
    |- myapp: an app in the website
        |- migrations: directory django uses for handling data models (classes) we create
        |- templates: HTML files with conditional rendering capabilities for templating
            |- *.html: various templates made in tutorial
        |- __init__.py: mark directory as module
        |- admin.py: file django uses for registering data models. Must register data models here
        |- apps.py: not sure yet
        |- models.py: file with our created data models. These are python classes
        |- tests.py: not sure yet
        |- urls.py: file for mapping HTTP requests to python functions to-be executed 
        |- views.py: file containing the python functions to-be executed upon a request. format is: 'request', html template to render (, optional_args)
    |- db.sqlite3: not sure yet
    |- manage.py: python file that acts as a command line tool for setting up files in the project
