#changer_site          
Django app folder.      

- Folder **'migrations'** contains the app's db migrations.               
- Folder **'static'** contains the app's static files (CSS, JS, img, fonts files, etc.).            
- Folder **'templates'* contains the app's templates files (HTML files).           
- Files **'admin.py'**, **'apps.py'**, **'models.py'**, and **'tests.py'** are standard Django files for adding apps, db models, and tests (not changed).             
- File **'urls.py'** contains URLs of all defined app's views and connects URL with a view:           
  - Path **''** is the app's start page. Only contains a link to the *'paraphrase'* page.          
  - Path **'paraphrase'** is the page where all logic and actions take place.             
- File **'views.py'** contains all app's views and defines actions for every defined in the app URL:               
  - View **'index'** connects *''* URL with the start page *'index.html'* and returns a *render()* function.                   
  - View **'paraphrase'** connects *'/paraphrase'* URL with the *'paraphrase.html'* page and processes query parameters in HTTP 'GET' method
      (*'tree'* - input constituency-based parse tree of sentences, *'limit'* (default: 20) - output variants display limit, *'print_options'* (string/tree/json) - variants of output view).
      Calls *'make_variations()'* function from *'tree.py'* file to transform input tree into output variations data, *'Data'* class to form proper data for Jinja to output.
      Returns *render()* function with *'info'* parameter.        
  - Class **'Data'** forms a proper and comfortable data view for Jinja to output.              
  - Class **'GrammarTree'** has a similar to *'paraphrase'* view logic but returns *Django Rest Framework response* for API in json format.             
- File **'tree.py'** contains all logic that generates a list of variations of sentence change from a string of sentence's constituency-based parse tree:
  - Function **make_tree()** generates a *nltk.ParentedTree* from a string of sentence's constituency-based parse tree if it is possible, else it returns an *error string*.
  - Function **get_children()** returns an *nltk.\<TreeType>.subtrees()* generator, which contains only a node's children.
  - Function **combinations()** returns a *dictionary of constituency-based parse tree's nodes* (every node has its number as a dict key), which could be replaced 
    and a list of all combinations of nodes replace (in number representation).            
  - Function **make_variations()** is a main function that contains logic to generate a list of variations of sentence change from a string of sentence's constituency-based parse tree 
    and it calls all other functions.
  - Construction *if \__name__ == "\__main__"* there is only for debugging and starting a *tree.py* file as an independent project.
