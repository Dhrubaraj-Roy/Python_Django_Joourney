# Monthly Challenges

A Django project built while learning URL dispatching, dynamic path converters, named URLs, HTTP redirects, and Django templates (variables, filters, and template tags).

## What it does

The application provides monthly challenges through dynamic URLs and Django templates:

1. **Challenges Index**: Visiting `/challenges/` renders `index.html`, displaying an unordered list of all 12 months. Each link is generated dynamically using the `{% for %}` loop and `{% url %}` template tag.
2. **Individual Challenge Pages**: Visiting `/challenges/january`, `/challenges/february`, etc. renders `challenges.html` with dynamic context:
   - `{{ text }}` renders the monthly challenge text.
   - `{{ month_name|title }}` dynamically sets the page title in the browser tab.
3. **Numeric Redirects with Named URLs**: Visiting `/challenges/1`, `/challenges/2`, etc. automatically redirects to the corresponding month URL (`/challenges/january`) using `HttpResponseRedirect` and `reverse()`.
4. **Error Handling**: Requests for months outside 1-12 or invalid month names return an HTTP 404 via `HttpResponseNotFound`.

## Template Architecture

Templates are namespaced inside the app under `challenges/templates/challenges/`:

- `index.html`: Loops through months passed from the view, generating clickable links with `{% url 'month-challenge' month %}`.
- `challenges.html`: Displays individual challenge text and dynamic page title using Django template variables.

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
- `http://127.0.0.1:8000/challenges/` (index page with month links)
- `http://127.0.0.1:8000/challenges/1` (redirects to `/challenges/january`)
- `http://127.0.0.1:8000/challenges/january` (renders January challenge template)
- `http://127.0.0.1:8000/challenges/13` (returns 404)
