# Monthly Challenges

A small Django project built while learning URL dispatching, dynamic path converters, named URLs, and HTTP redirects.

## What it does

The application provides monthly challenge goals based on the URL you visit:

1. **Challenges Index**: Visiting `/challenges/` displays an HTML list of all 12 months. Each month is a clickable link leading to its challenge page.
2. **Named URLs**: Visiting `/challenges/january`, `/challenges/february`, etc. displays the challenge text for that specific month.
3. **Numeric Redirects with Named URL Lookup**: Visiting `/challenges/1`, `/challenges/2`, etc. redirects to the corresponding month URL (`/challenges/january`) using Django's `HttpResponseRedirect` and `reverse()`. The path is generated dynamically using named routes rather than hardcoded strings.
4. **Error Handling**: If an invalid month name or a number outside 1-12 is passed, the server responds with a 404 status via `HttpResponseNotFound`.

## URL Configuration

- `/challenges/` - Handled by `index` (`name="index"`), renders an unordered list of months with links.
- `/challenges/<int:month>` - Handled by `monthly_challenge_by_number`, redirects to the month name via `reverse()`.
- `/challenges/<str:month>` - Handled by `monthly_challenge` (`name="month-challenge"`), returns the text response.

Note: The integer path is declared before the string path in `challenges/urls.py` so Django matches numbers before treating them as generic strings.

## Running the project locally

Make sure you have Django installed in your environment, then run:

```bash
python manage.py runserver
```

Open your browser and test:
- `http://127.0.0.1:8000/challenges/` (list of all months with links)
- `http://127.0.0.1:8000/challenges/1` (redirects to `/challenges/january`)
- `http://127.0.0.1:8000/challenges/march`
- `http://127.0.0.1:8000/challenges/13` (returns 404)
