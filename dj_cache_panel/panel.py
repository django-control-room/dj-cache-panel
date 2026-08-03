from dj_control_room_base.core import PanelPlugin


class CachePanel(PanelPlugin):
    name = "Cache Panel"
    description = "Inspect and manage Django cache backends"
    icon = "layers"
    icon_color = "purple"
    features = [
        "Browse configured cache instances and their capabilities",
        "Search and browse keys for backends that support it",
        "View, add, edit, and delete individual cache keys",
        "Flush an entire cache instance",
    ]

    app_name = "dj_cache_panel"
    docs_url = "https://github.com/django-control-room/dj-cache-panel"
    pypi_url = "https://pypi.org/project/dj-cache-panel/"

    def get_url_name(self):
        return "index"

    def get_config(self):
        from .conf import panel_config

        return panel_config
