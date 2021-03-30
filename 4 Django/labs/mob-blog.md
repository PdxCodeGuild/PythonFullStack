


# Blog

## Models

- BlogPost
  - title (CharField)
  - body (TextField)
  - created_date (DateTimeField)

## Views

- index
  - List of blog posts using an [accordian](https://getbootstrap.com/docs/5.0/components/accordion/) or [collapsible](https://materializecss.com/collapsible.html).
  - Form for creating a new blog post.
  - Search (enter some text, press 'search' and show only blog posts whose title [contains](https://docs.djangoproject.com/en/3.1/ref/models/querysets/#icontains) the search term)
- create_post
  - receive the form submission from the index page, create a new blog post

