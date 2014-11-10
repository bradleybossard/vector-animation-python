import pip
for package in pip.get_installed_distributions():
    name = package.project_name # SQLAlchemy, Django, Flask-OAuthlib
    key = package.key # sqlalchemy, django, flask-oauthlib
    module_name = package._get_metadata("top_level.txt") # sqlalchemy, django, flask_oauthlib
    location = package.location # virtualenv lib directory etc.
    version = package.version # version number
    print name
    #print key
    print " " + str(module_name)
    print " " + str(location)
    print " " + str(version)
