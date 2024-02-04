# Django Squashmigrations Example

Example project for these talks:

- [DjangoCon US 2023](https://slides.dennybiasiolli.com/index-django-squashmigrations-djangocon23.html)

- [GDG Cuneo 2023](https://slides.dennybiasiolli.com/index-django-migrations-gdg23.html)

- [FOSDEM 2024](https://slides.dennybiasiolli.com/index-django-squashmigrations-fosdem24.html)

## Branches

- `django-settings-migrate` ([PR #4](https://github.com/dennybiasiolli/django-squashmigrations-example/pull/4))

    Example using the `MIGRATE = False` approach to avoid running migrations in tests.

- `squashing-migrations` ([PR #2](https://github.com/dennybiasiolli/django-squashmigrations-example/pull/2))

    Example of standard squashing migrations.

- `recreating-migrations` ([PR #3](https://github.com/dennybiasiolli/django-squashmigrations-example/pull/3))

    Example of recreating migrations from scratch.


## How to run the project

```bash
# clone / enable virtualenv, etc...
# ...
# then install requirements
pip install -r requirements.txt

# choose the branch you want to examine
# git checkout ...

# run and measure tests
time python manage.py test
```
