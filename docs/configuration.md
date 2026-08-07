# Configuration

Django Cache Panel works out of the box with your existing Django `CACHES` configuration. Advanced configuration is optional.

## Basic Configuration

The only required configuration is your Django `CACHES` setting:

```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'redis': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    },
}
```

## Advanced Configuration

For advanced use cases, you can customize behavior with `DJ_CACHE_PANEL_SETTINGS`.
A full annotated example:

```python
DJ_CACHE_PANEL_SETTINGS = {
    # CSS: load built-in styles and/or inject your own
    "LOAD_DEFAULT_CSS": True,
    # Static paths are relative to app's static/ dir (e.g. 'myapp/css/overrides.css'
    # for a file at myapp/static/myapp/css/overrides.css). Full URLs also accepted.
    "EXTRA_CSS": [],

    # Optional: completely replace the default backend-to-panel mapping
    # "BACKEND_PANEL_MAP": {}
    #
    # Optional: extend or override specific backend-to-panel mappings
    # Panel classes can be specified as:
    #   - Simple class name (e.g., "RedisCachePanel") - for built-in panels
    #   - Full module path (e.g., "myapp.panels.CustomCachePanel") - for custom panels
    "BACKEND_PANEL_EXTENSIONS": {
        # Example: Map a custom backend to a custom panel class
        # "myapp.backends.CustomCache": "myapp.panels.CustomCachePanel",
        # Example: Override a built-in backend mapping
        # "django.core.cache.backends.redis.RedisCache": "myapp.panels.MyRedisCachePanel",
    },
    # Optional: per-cache settings overrides
    # Typically used to lock down a cache instance to only certain abilities
    "CACHES": {
        "redis": {
            "abilities": {  # Optional: override the abilities for this cache instance
                # "query": True,
                # "get_key": True,
                # "delete_key": True,
                # "edit_key": True,
                # "add_key": True,
                # "flush_cache": True,
            },
        }
    },
}
```

The sections below cover each option in more detail.

### Custom Panel Mappings

Map custom cache backends to panel classes:

```python
DJ_CACHE_PANEL_SETTINGS = {
    "BACKEND_PANEL_EXTENSIONS": {
        # Map custom backend to custom panel
        "myapp.backends.CustomCache": "myapp.panels.CustomCachePanel",
        
        # Override built-in backend
        "django.core.cache.backends.redis.RedisCache": "myapp.panels.MyRedisPanel",
    },
}
```

Panel classes can be specified as:

- **Simple name**: `"RedisCachePanel"` (looked up in `dj_cache_panel.cache_panel`)
- **Full path**: `"myapp.panels.CustomCachePanel"` (imported dynamically)

### Per-Cache Ability Overrides

Restrict operations for specific caches:

```python
DJ_CACHE_PANEL_SETTINGS = {
    "CACHES": {
        "production_cache": {
            "abilities": {
                "query": True,
                "get_key": True,
                "delete_key": False,  # Disable deletes
                "edit_key": False,    # Disable edits
                "add_key": False,     # Disable adds
                "flush_cache": False, # Disable flush
            },
        },
    },
}
```

Available abilities:

- `query`: List/search keys with patterns
- `get_key`: View individual key values
- `delete_key`: Delete keys
- `edit_key`: Modify key values
- `add_key`: Create new keys
- `flush_cache`: Clear all cache entries

## URLs Configuration

By default, the panel is accessible at `/admin/dj-cache-panel/`. You can change this:

```python
# urls.py
urlpatterns = [
    path('admin/cache/', include('dj_cache_panel.urls')),  # Custom path
    path('admin/', admin.site.urls),
]
```

## Security

Django Cache Panel uses Django's built-in admin authentication:

- Only staff users (`is_staff=True`) can access the panel
- All views require authentication via `@staff_member_required`
- No additional security configuration needed

To restrict access further, use per-cache ability overrides or implement custom panel classes.

## CSS Customization

### `LOAD_DEFAULT_CSS`

**Type:** `bool`  
**Default:** `True`  
**Description:** Whether to load the built-in Cache Panel stylesheet. Set to `False` to use your own styles from scratch.

### `EXTRA_CSS`

**Type:** `list[str]`  
**Default:** `[]`  
**Description:** Additional stylesheets to load after the default CSS. Accepts static file paths or full URLs.

Static file paths are **relative to your app's `static/` subdirectory** (same convention as Django's `{% static %}` tag). A file at `myapp/static/myapp/css/overrides.css` is referenced as `myapp/css/overrides.css`.

```python
DJ_CACHE_PANEL_SETTINGS = {
    'LOAD_DEFAULT_CSS': True,
    'EXTRA_CSS': [
        # File lives at: myapp/static/myapp/css/overrides.css
        'myapp/css/overrides.css',
        # Full URLs are also supported
        'https://cdn.example.com/theme.css',
    ],
}
```
