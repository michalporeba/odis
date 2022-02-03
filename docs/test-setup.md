# Test Setup in Django Projects

```bash
pipenv install pytest-django
```

Create `pytest.ini` in the root folderof the project.
```ini
[pytest]
DJANGO_SETTINGS_MODULE = yourproject.settings
python_files = tests.py test_*.py *_tests.py
```
the above casing appears to be important. 

Run the tests with `pytest` command directly. 