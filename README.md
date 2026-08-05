[![Django Control Room Panel](https://img.shields.io/badge/Django%20Control%20Room-Panel-0c4b33?logo=django)](https://github.com/django-control-room/dj-control-room)
[![Tests](https://github.com/django-control-room/dj-cache-panel/actions/workflows/test.yml/badge.svg)](https://github.com/django-control-room/dj-cache-panel/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/django-control-room/dj-cache-panel/branch/main/graph/badge.svg)](https://codecov.io/gh/django-control-room/dj-cache-panel)
[![PyPI version](https://badge.fury.io/py/dj-cache-panel.svg)](https://badge.fury.io/py/dj-cache-panel)
[![Python versions](https://img.shields.io/pypi/pyversions/dj-cache-panel.svg)](https://pypi.org/project/dj-cache-panel/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://img.shields.io/pypi/dm/dj-cache-panel.svg)](https://pypi.org/project/dj-cache-panel/)


# Django Cache Panel

A universal cache inspector for Django.

![Django Cache Panel - Instance List](https://raw.githubusercontent.com/django-control-room/dj-cache-panel/main/images/instance_list.png)

**Compatible with [dj-control-room](https://github.com/django-control-room/dj-control-room).** Register this panel in the Control Room to manage it from a centralized dashboard.

- **Official site:** [djangocontrolroom.com](https://djangocontrolroom.com)
- **Project repo:** [dj-control-room](https://github.com/django-control-room/dj-control-room)

## Docs

[https://django-control-room.github.io/dj-cache-panel/](https://django-control-room.github.io/dj-cache-panel/)

## Features

- **Browse Cache Instances**: View all configured cache backends from your `CACHES` setting
- **Abilities Matrix**: See at a glance which operations each cache supports (Query, Get, Delete, Flush)
- **Key Search**: Search and browse cache keys with wildcard patterns (for supported backends)
- **Value Preview**: View cache values directly in search results
- **Pagination**: Navigate through large sets of keys efficiently
- **Admin Integration**: Seamlessly integrates with Django's admin interface
- **Secure**: Only accessible to staff users
- **Backend Agnostic**: Works with any Django cache backend (with varying feature support)


## Requirements

- Python 3.9-3.14
- Django 4.2+


## Screenshots

### Django Admin Integration
Seamlessly integrated into your Django admin interface. A new section for dj-cache-panel
will appear in the same places where your models appear.

**NOTE:** This application does not actually introduce any model or migrations.

![Admin Home](https://raw.githubusercontent.com/django-control-room/dj-cache-panel/main/images/admin_home.png)

### Caches Overview
Get a list of all your caches as well as the allowed capabilities for each cache

![Instance Overview](https://raw.githubusercontent.com/django-control-room/dj-cache-panel/main/images/instance_list.png)

### Key Search

![Key Search](https://raw.githubusercontent.com/django-control-room/dj-cache-panel/main/images/key_search.png)

### Key Edits/Adds

![Key Detail](https://raw.githubusercontent.com/django-control-room/dj-cache-panel/main/images/key_detail.png)


## Installation

```bash
pip install dj-cache-panel dj-control-room
```

Optional Valkey support (requires Python 3.10+):

```bash
pip install dj-cache-panel[valkey] dj-control-room
```

Add it to `INSTALLED_APPS`, include its URLs, and migrate:

```python
INSTALLED_APPS = [
    # ...
    "dj_control_room_base",
    "dj_cache_panel",
    "dj_control_room",
    # ...
]
```

```python
urlpatterns = [
    path("admin/dj-control-room-base/", include("dj_control_room_base.urls")),
    path("admin/dj-cache-panel/", include("dj_cache_panel.urls")),
    path("admin/dj-control-room/", include("dj_control_room.urls")),
    path("admin/", admin.site.urls),
]
```

The panel reads your existing Django `CACHES` setting. no extra instance config required for most projects. Advanced options (backend panel mappings, per-cache ability overrides, CSS) are covered in [Configuration](https://django-control-room.github.io/dj-cache-panel/configuration/).

```bash
python manage.py migrate
```

Then visit `/admin/` and look for the "DJ CACHE PANEL" section.

For the full walkthrough and production recommendations, see the [Installation](https://django-control-room.github.io/dj-cache-panel/installation/) and [Configuration](https://django-control-room.github.io/dj-cache-panel/configuration/) docs. See [Scopes](https://django-control-room.github.io/dj-cache-panel/scopes/) for per-view permission scopes.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Development Setup

Want to contribute or set up the project for local development? See [docs/development.md](docs/development.md) for prerequisites, Docker/virtualenv setup, running the example project, and the test suite.
