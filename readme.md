# Monthly Challenges

A Django project built while learning URL dispatching, dynamic path converters, named URLs, HTTP redirects, template inheritance, partial template includes, and custom 404 error handling.

## What it does

The application provides monthly challenges through dynamic URLs and Django templates:

1. **Challenges Index**: Visiting `/challenges/` renders `index.html`, displaying an unordered list of all 12 months. Each link is generated dynamically using a `{% for %}` loop and the `{% url %}` template tag.
2. **Individual Challenge Pages**: Visiting `/challenges/january`, `/challenges/february`, etc. renders `challenges.html` with dynamic context:
   - `{{ text }}` renders the monthly challenge text.
   - `{{ month_name|title }}` sets the page title in the browser tab.
   - Conditional rendering (`{% if text is not None %}`) displays a fallback notice if a month has no active challenge (e.g., December).
3. **Reusable Navigation Header**: A partial template (`header.html`) is included across pages to provide consistent site-wide navigation back to "All Challenges".
4. **Numeric Redirects with Named URLs**: Visiting `/challenges/1`, `/challenges/2`, etc. automatically redirects to the corresponding month URL (`/challenges/january`) using `HttpResponseRedirect` and `reverse()`.
5. **Custom 404 Error Page**: Requests for months outside 1-12 or invalid URLs raise `Http404()`, which renders a custom `404.html` template when `DEBUG = False`.

## Template Architecture & Inheritance

Templates follow a clean hierarchy using inheritance (`{% extends %}`) and partials (`{% include %}`):

- **Root Templates (`templates/`)**:
  - `base.html`: Global HTML skeleton defining `<head>`, `<title>`, and block tags: `{% block page_title %}` and `{% block content %}`.
  - `404.html`: Custom error page extending `base.html` and including the navigation header.
  - Registered in `monthly_challenges/settings.py` via `TEMPLATES['DIRS'] = [BASE_DIR / "templates"]`.

- **App Templates (`challenges/templates/challenges/`)**:
  - `index.html`: Extends `base.html`, includes `header.html`, and loops over months.
  - `challenges.html`: Extends `base.html`, includes `header.html`, and renders the challenge text or fallback message.
  - `includes/header.html`: Reusable partial template providing top-level navigation.

## URL Configuration

- `/challenges/` - Handled by `index` (`name="index"`), renders `index.html`.
- `/challenges/<int:month>` - Handled by `monthly_challenge_by_number`, redirects to the month name via `reverse()`.
- `/challenges/<str:month>` - Handled by `monthly_challenge` (`name="month-challenge"`), renders `challenges.html`.

Note: The integer route is registered before the string route in `challenges/urls.py` so numbers match numeric redirects rather than generic month strings.

## Running the project locally

Make sure you have Django installed in your environment, then run:

```bash
python manage.py runserver
```

Open your browser and test:
- `http://127.0.0.1:8000/challenges/` (index page extending base layout)
- `http://127.0.0.1:8000/challenges/1` (redirects to `/challenges/january`)
- `http://127.0.0.1:8000/challenges/january` (renders January challenge with header)
- `http://127.0.0.1:8000/challenges/december` (renders fallback "no challenge" message)
- `http://127.0.0.1:8000/challenges/13` (renders custom 404 template with header)
