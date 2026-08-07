from dj_control_room_base.core import PanelPlaceholderModel


class CachePanelPlaceholder(PanelPlaceholderModel):
    """
    This is a fake model used to create an entry in the admin panel for the cache panel.
    When we register this app with the admin site, it is configured to simply load
    the cache panel templates.
    """

    class Meta(PanelPlaceholderModel.Meta):
        verbose_name = "DJ Cache Panel"
        verbose_name_plural = "DJ Cache Panel"
