[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-f4981d0f882b2a3f0472912d15f9806d57e124e0fc890972558857b51b24a6f9.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=10025588)
# First web scraper

A step-by-step guide to writing a web scraper with Python.

* Documentation: [first-web-scraper-umd.rtfd.org](https://first-web-scraper-umd.readthedocs.io/en/latest/)

### Contributing to the documentation

After installing the repository, the Sphinx documentation can be edited in the
``docs`` directory and published to ReadTheDocs by pushing changes to the ``master`` branch.

First install the requirements.

```bash
$ pipenv install
```

Fire up the test server, which will automatically update to show changes made
to the restructured text files in the ``docs`` directory.

```bash
$ make docs
```

Open ``http://localhost:8000`` in your browser and start making changes.
