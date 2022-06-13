# Django Templates

- Put the variable inside {{ }} brackets
- You can also create variables directly in the template, by using the {% with %} template tag

```html
{% with firstname="Tobias" %}
<h1>Hello {{ firstname }}, how are you?</h1>
```

- We use the Django template tag {% for %} to loop through the members.

## Template Tags / Django if elif else Tag
- In Django templates, you can perform programming logic like executing if statements and for loops.

- These keywords, if and for, are called "template tags" in Django.

- To execute template tags, we surrond them in ``{% %}`` brackets.

```html
{% if greeting == 1 %}
  <h1>Hello</h1>
{% elif greeting == 2 %}
  <h1>Hello Boys!</h1>  
{% else %}
  <h1>Bye</h1>
{% endif %}
```

## Django for Tag

- A for loop is used for iterating over a sequence, like looping over items in an array, a list, or a dictionary.

Loop through the items of a list:
```html
{% for x in fruits %}
  <h1>{{ x }}</h1>
{% endfor %}
```

Loop through a list of dictionaries:
```html
{% for x in cars %}
  <h1>{{ x.brand }}</h1>
  <p>{{ x.model }}</p>
  <p>{{ x.year }}</p>
{% endfor %} 

```

Data From a Model

- Data in a model is like a table with rows and columns.
```
<QuerySet [
  {
    'id': 1,
    'firstname': 'Emil',
    'lastname': 'Refsnes'
  },
  {
    'id': 2,
    'firstname': 'Tobias',
    'lastname': 'Refsnes'
  },
  {
    'id': 3,
    'firstname': 'Linus',
    'lastname': 'Refsnes'
  },
  {
    'id': 4,
    'firstname': 'Lene',
    'lastname': 'Refsnes'
  },
  {
    'id': 5,
    'firstname': 'Stalikken',
    'lastname': 'Refsnes'
  }
]> 
```
When we fetch data from the model, it comes as a QuerySet object, a list with dictionaries:

Loop through items fetched from a database:
```html
{% for x in members %}
  <h1>{{ x.id }}</h1>
  <p>
    {{ x.firstname }}
    {{ x.lastname }}
  </p>
{% endfor %} 

```

## Django comment Tag
- Comments allows you to have sections of code that should be ignored.
```html
<h1>Welcome Everyone</h1>
{% comment %}
  <h1>Welcome ladies and gentlemen</h1>
{% endcomment %}
```

- Smaller Comments

    You can also use the {# ... #} tags

    ```html
    <h1>Welcome{# Everyone#}</h1>
    ```

## Django cycle Tag

- The cycle tag allows you to do different tasks for different iterations.
- The cycle tag takes arguments, the first iteration uses the first argument, the second iteration uses the second argument etc.

```html
<ul>
  {% for x in members %}
    <li style='background-color:{% cycle 'lightblue' 'pink' 'yellow' 'coral' 'grey' %}'>
      {{ x.firstname }}
    </li>
  {% endfor %}
</ul> 
```


## Django extends Tag

**Extends**

- The extends tag allows you to add a parent template for the current template.

- This means that you can have one master page that acts like a parent for all other pages

- You put placeholders in the master template, telling Django where to put which content.

- Django uses the ``{% block %}`` tag, to create placeholders

``master.html``

```html
<html>
<body>

{% block myheading %}
{% endblock %}

{% block mymessage %}
{% endblock %}

</body>
</html> 
```

``template.html``
```html
{% extends 'mymaster.html' %}

{% block myheading %}
  <h1>Members</h1>
{% endblock %}

{% block mymessage %}
  <ul>
    {% for x in members %}
      <li>{{ x.firstname }}</li>
    {% endfor %}
  </ul>
{% endblock %} 
```


## Django include Tag
- The include tag allows you include a template inside the current template.

- This is useful when you have a block of content that are the same for many pages.

``footer.html:``

```html
<p>You have reach the bottom of this page, thank you for your time.</p>

```
``template.html:``

```html
<h1>Hello</h1>

<p>This page contains a footer in a template.</p>

{% include 'footer.html' %} 
```
## variables in Include
- You can send variables into the template by using the with keyword.

``mymenu.html:``

```html
<div>HOME | {{ me }} | ABOUT | FORUM | {{ sponsor }}</div>
```

``template.html:``

```html
<!DOCTYPE html>
<html>
<body>

{% include mymenu.html with me="TOBIAS" sponsor="W3SCHOOLS" %}

<h1>Welcome</h1>

<p>This is my webpage</p>

</body>
</html> 
```