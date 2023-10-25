# Tarea 1

## Preparación

1. Haga un fork de este repo en su propia cuenta en GitHub.
2. Clone el fork en Replit
 

## Paso 1

Modifique el archivo `main.py` en la línea 3 dejándola así:

```python
from flask import Flask, render_template, request, url_for, redirect

```

Luego agregue la siguiente ruta al final del archivo `main.py`:

```python
# ...


@app.route('/create/', methods=('GET', 'POST'))
def create():
    return render_template('create.html')

```


Agregue el cambio al área stage de git con el siguiente comando en la shell de Replit:

```
git add main.py
```

# Paso 2

En la carpeta templates agregue el archivo `create.html` y agregue el siguiente código en este:

```html
{% extends 'base.html' %}

{% block content %}
    <h1>{% block title %} Add a New Book {% endblock %}</h1>
    <form method="post">
        <p>
            <label for="title">Title</label>
            <input type="text" name="title"
                   placeholder="Book title">
            </input>
        </p>

        <p>
            <label for="author">Author</label>
            <input type="text" name="author"
                   placeholder="Book author">
            </input>
        </p>

        <p>
            <label for="pages_num">Number of pages</label>
            <input type="number" name="pages_num"
                   placeholder="Number of pages">
            </input>
        </p>
        <p>
        <label for="review">Review</label>
        <br>
        <textarea name="review"
                  placeholder="Review"
                  rows="15"
                  cols="60"
                  ></textarea>
        </p>
        <p>
            <button type="submit">Submit</button>
        </p>
    </form>
{% endblock %}
```

Agregue la carpeta templates al stage:  

  git add templates

Ahora haga un commit de la siguiente forma:

  git commit -m "feat: agrega el endpoint create"

Luego de esto haga push y revise que sus cambios se reflejan en GitHub.

