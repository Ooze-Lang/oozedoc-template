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

Open <http://127.0.0.1:8000/>. Keep the server running while editing files in `mkdoc/docs/` from VS Code;
MkDocs rebuilds the site and reloads the browser when they change. Search works in the local preview too.

In VS Code, run **Tasks: Run Task** and select **Docs: Preview (live reload)**. The task installs dependencies
and starts the same server in the integrated terminal. Stop the task to shut it down.

To generate a static site for hosting:

```sh
mkdoc/.venv/bin/python -m mkdocs build -f mkdoc/mkdocs.yml
```

The output is `mkdoc/site/`. Add blog posts under `mkdoc/docs/blog/posts/` with date metadata:

```md
---
date: 2026-10-03
---

# Post title

Post content.
```

The existing repository `docs/` directory contains internal notes and is separate from this site.

Use `ooze` as the language for fenced Ooze examples. The dependency install above also installs the
local Pygments lexer from `mkdoc/pygments-ooze`, so preview and static builds highlight Ooze automatically.
Run the install command from the repository root; the local package path is relative to that directory.

Standard-library API pages come from `/** ... */` module overviews and `///` declaration comments in
`ooze/std/`. Keep examples short and document the public types, trait methods, and functions in source.
Enum pages show the data type separately and list values in a table. Place `///` or `/** ... */`
comments before individual enum values (or `///` after their commas) to describe each row.
Collapsed function headers show parameter and return types to distinguish overloads; field headers
show their types. Full signatures, defaults, constraints, and descriptions remain inside each entry.
To regenerate every page:

```sh
mkdoc/.venv/bin/python -m pip install -r tools/requirements.txt
mkdoc/.venv/bin/python tools/gen_stdlib_docs.py --replace-all
```

The generator prints nested navigation YAML for the Standard Library section of `mkdocs.yml`.
It omits test modules and bootstrap files, folds core string declarations into `string`, and puts the
shared transport declarations on the `net/socket` and `net/tls` pages. `--replace-all` also removes
previously generated pages for ignored files. Private declarations and package-only fields are hidden.

In VS Code, run **Tasks: Run Task** and select **Docs: Generate all stdlib docs**. The task installs
the dependencies and regenerates every API page using `cmake-build-release/ooze_cpp`, which must be built first.
To regenerate only the active `.oz` file, select **Docs: Generate current stdlib file docs**.
For files under `ooze/std`, it replaces the matching page under `mkdoc/docs/stdlib/gen`, preserving
subdirectories (for example, `ooze/std/net/socket.oz` updates `mkdoc/docs/stdlib/gen/net/socket.md`).
