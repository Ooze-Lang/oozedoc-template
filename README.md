# Ooze documentation site

From the repository root, create a Python virtual environment and install the site dependency:

```sh
python3 -m venv mkdoc/.venv
mkdoc/.venv/bin/python -m pip install -r mkdoc/requirements.txt
```

Start the local preview server:

```sh
mkdoc/.venv/bin/python -m mkdocs serve -f mkdoc/mkdocs.yml
```

Open <http://127.0.0.1:8000/>. Keep the server running while editing files in `mkdoc/docs/`.
MkDocs rebuilds the site and reloads the browser when they change. 

Search plugin is enabled and works for searching during local development.

To generate a static site for hosting:

```sh
mkdoc/.venv/bin/python -m mkdocs build -f mkdoc/mkdocs.yml
```

The output is `mkdoc/site/`.

The existing repository `docs/` directory contains internal notes and is separate from this site.

Use `ooze` as the language for fenced Ooze examples. Syntax highlighting is provided by Pygments in `pygments-ooze`.
Run the install command from the repository root; the local package path is relative to that directory.
