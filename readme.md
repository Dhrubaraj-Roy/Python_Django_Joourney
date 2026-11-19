# Monthly Challenges

A small Django project built while learning URL dispatching, dynamic path converters, and HTTP redirects.

## What it does

The application provides monthly challenge goals based on the URL you visit:

1. **Named URLs**: Visiting `/challenges/january`, `/challenges/february`, etc. displays the challenge text for that specific month.
2. **Numeric Redirects**: Visiting `/challenges/1`, `/challenges/2`, etc. automatically redirects to the corresponding month URL (`/challenges/january`) using Django's `HttpResponseRedirect`.
3. **Error Handling**: If an invalid month name or a number outside 1-12 is passed, the server responds with a 404 status via `HttpResponseNotFound`.

## URL Configuration

- `/challenges/<int:month>` - Handled by `monthly_challenge_by_number`, redirects to the month name.
- `/challenges/<str:month>` - Handled by `monthly_challenge`, looks up and returns the text response.

Note: The integer path is declared first in `challenges/urls.py` so Django matches numbers before treating them as generic strings.

## Running the project locally

Make sure you have Django installed in your environment, then run:

```bash
python manage.py runserver
```

Open your browser and test:
- `http://127.0.0.1:8000/challenges/1` (should redirect to `/challenges/january`)
- `http://127.0.0.1:8000/challenges/march`
- `http://127.0.0.1:8000/challenges/13` (should return 404)
