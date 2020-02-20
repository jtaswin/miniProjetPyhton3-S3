#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

if str(form.getvalue('name')) == "None":
    print("Aucun nom defini")
else:
    print(form.getvalue("name"))

html = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
    <form action="/testForm.py" method="post">
        <input type="text" name="name" value="Votre nom" />
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form> 
</body>
</html>
"""

print(html)