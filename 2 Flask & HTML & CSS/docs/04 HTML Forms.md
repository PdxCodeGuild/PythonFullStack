
# HTML Forms

- [Overview](#overview)
- [Attributes](#attributes)
  - [The Placeholder Attribute](#the-placeholder-attribute)
  - [The Disabled Attribute](#the-disabled-attribute)
  - [The Required Attribute](#the-required-attribute)
  - [The Pattern Attribute](#the-pattern-attribute)

## Overview

A `form` is an HTML element that allows users to transmit data to a server. You can read more about forms [here](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Your_first_HTML_form). There are 5 important parts to a form:

1. The `action` is the path or url to which the form's data will be submitted.
2. The `method` is the HTTP method to send the request in (POST, GET).
3. The `input` elements inside a form need name attributes, which will be used to retreive the data on the back-end.
4. The `<button type="submit">` or `<input type="submit">` will submit the form when clicked.
5. The `{% csrf_token %}` will insert a token that protects against [Cross-site request forgeries](https://en.wikipedia.org/wiki/Cross-site_request_forgery).

```html
<form action="/mypath/" method="post">
    {% csrf_token %}
    <input type="text" name="myname"/>
    <button type="submit">save</button>
</form>
```

Let's take a look back at [HTML forms](../../2%20HTML+CSS/docs/03%20-%20HTML%20Forms.md). You don't have to do anything special to use forms in Django. The `input` elements need `name` attributes, the `action` attribute of the form needs to point to a view. When you submit the data, the form will gather all the `name` attributes from the `input` fields and associate them with each `input`'s `value`.

```html
<form action="{% url 'contacts:save_contact' %}" method="post">
    {% csrf_token %}
    <input type="text" name="contact_name"/>
    <input type="number" name="contact_age"/>
    <button type="submit">save contact</button>
</form>
```

Django will take the name-value pairs from the request and put them into a dictionary-like object `request.POST`. You can then access those values from the view using the value of the `name` attribute as a key.


## Attributes

### The Placeholder Attribute

You can also add a `placeholder` attribute to show some text in the 'background' of the input field. This text disappears when a value is entered.

```html
<input type="text" name="name" value="jane" placeholder="enter your name"/>
```

### The Disabled Attribute

To disabled an input field, you can add the `disabled` attribute without any parameters. This will prevent the user from entering any value into the input field. It doesn't matter what the value of the attribute is, as long as it's present, the input will be disabled.

```html
<input type="text" name="name" value="jane" disabled/>
```

### The Required Attribute

You can place the attribute `required` with no value to prevent the form from being submitted without that field being filled. Like `disabled`, the attribute doesn't need a value.

```html
<input type="text" name="name" required/>
```


### The Pattern Attribute

HTML5 brought the `pattern` attribute, which enables you to do validation entirely within HTML. You only have to enter a regular expression into the `pattern` attribute. If the user tries to submit the form and the given input doesn't match the pattern, a message will pop up containing the text in the `title` attribute.

```html
<form action="..." method="...">
    <input type="text" pattern="[a-z]{1,15}" title="username must be between 1 and 15 characters, all lowercase" required/>
    <button type="submit">submit</button>
</form>
```











