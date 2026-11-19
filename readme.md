# Monthly Challenges

A Django project built while learning URL dispatching, dynamic path converters, named URLs, HTTP redirects, template inheritance, and template tags.

## What it does

The application provides monthly challenges through dynamic URLs and Django templates:

1. **Challenges Index**: Visiting `/challenges/` renders `index.html`, displaying an unordered list of all 12 months. Each link is generated dynamically using a `{% for %}` loop and the `{% url %}` template tag.
2. **Individual Challenge Pages**: Visiting `/challenges/january`, `/challenges/february`, etc. renders `challenges.html` with dynamic context:
   - `{{ text }}` renders the monthly challenge text.
   - `{{ month_name|title }}` sets the page title in the browser tab.
   - Conditional rendering (`{% if text is not None %}`) displays a fallback notice if a month has no active challenge (e.g., December).
3. **Numeric Redirects with Named URLs**: Visiting `/challenges/1`, `/challenges/2`, etc. automatically redirects to the corresponding month URL (`/challenges/january`) using `HttpResponseRedirect` and `reverse()`.
4. **Error Handling**: Requests for months outside 1-12 or invalid month names return an HTTP 404 via `HttpResponseNotFound`.

## Template Architecture & Inheritance

Templates use a shared layout structure through template inheritance:

- **Root Base Template (`templates/base.html`)**:
  - Serves as the global HTML skeleton defining the `<head>`, `<title>`, and block tags: `{% block page_title %}` and `{% block content %}`.
  - Located at the project root and registered in `monthly_challenges/settings.py` via `TEMPLATES['DIRS'] = [BASE_DIR / "templates"]`.

- **App Templates (`challenges/templates/challenges/`)**:
  - `index.html`: Extends `base.html`, injects the "All Challenges" title into `page_title`, and renders the list of months inside `content`.
  - `challenges.html`: Extends `base.html`, injects the dynamic month title into `page_title`, and renders the challenge text or fallback message inside `content`.

## URL Configuration

- `/challenges/` - Handled by `index` (`name="index"`), renders `index.html`.
- `/challenges/<int:month>` - Handled by `monthly_challenge_by_number`, redirects to the month name using `reverse()`.
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
- `http://127.0.0.1:8000/challenges/january` (renders January challenge)
- `http://127.0.0.1:8000/challenges/december` (renders fallback "no challenge" message)
- `http://127.0.0.1:8000/challenges/13` (returns 404)
