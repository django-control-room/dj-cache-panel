# Scopes

Dj Cache Panel splits its permission checks into **scopes**: named checkpoints passed to `@panel_config.permission_required(scope)`. Every scope inherits the panel-wide `ALLOWED_GROUPS`/`REQUIRE_SUPERUSER` rule by default; a scope only behaves differently once you add an entry for it under `SCOPE_PERMISSIONS` in `DJ_CACHE_PANEL_SETTINGS`.

See the [Permissions and Scopes guide](https://djangocontrolroom.com/guides/control-room-permissions-and-scopes) for the full model.

## Reference

| Scope | Type | Protects | Default behavior |
|---|---|---|---|
| `cache_list` | View | `index` view: browse configured Django cache backends | Any staff user |
| `key_search` | View | `key_search` view: browse/search keys in a selected cache (also handles flush-cache POSTs when supported) | Any staff user |
| `key_detail` | View | `key_detail` view: view a key's value and (when abilities allow) edit or delete it | Any staff user |
| `key_add` | View | `key_add` view: create a new key | Any staff user |

This panel does not currently register MCP tools, so there are no `agent_*` scopes.

## Example: read-only browsing, restricted writes

Per-cache ability overrides (e.g. `delete_key`, `edit_key`, `flush_cache`) hide mutating UI controls, but scopes let you go further and deny access to the write-capable views entirely for some groups:

```python
DJ_CACHE_PANEL_SETTINGS = {
    # Panel-wide default: any staff member can browse caches and keys
    'ALLOWED_GROUPS': [],

    'SCOPE_PERMISSIONS': {
        # Only platform admins may open the key detail page (which is also
        # where edit/delete land), create new keys, or reach the search
        # page that hosts the flush-cache action.
        'key_detail': {'ALLOWED_GROUPS': ['platform-admins']},
        'key_add': {'ALLOWED_GROUPS': ['platform-admins']},
        'key_search': {'ALLOWED_GROUPS': ['platform-admins']},
    },
}
```

Any scope not mentioned in `SCOPE_PERMISSIONS` simply falls back to the panel-wide rule, so you only ever need to write down the exceptions.

See [Configuration](configuration.md) for the rest of the panel's settings, including per-cache ability overrides.
