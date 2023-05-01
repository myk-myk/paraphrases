#text_changer           
Django project folder.

Files 'asgi.py' and 'wsgi.py' are standart Django files for defining ASGI and WSGI callables.               
File 'settings.py' contains settings information for project (all installed apps, templates, static and db files directories etc).         
File 'urls.py' contains a list of defined URLs' configurations which routes URLs to the app views:       
    Path 'admin/' routes to the standart Django admin panel.                   
    Path '' routes to the app's start webpage and function 'include' adds all defined in the '<app_name>/urls.py' file URLs.           
    Path 'api/v1/grammar_tree' routes to the Django Rest Framework (DRF) APIView page.
