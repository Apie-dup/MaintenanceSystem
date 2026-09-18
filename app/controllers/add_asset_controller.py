from app.dialogs.asset_dialog import AssetDialog


class AddAssetController(AssetDialog):
    """Compatibility wrapper for the legacy Add Asset controller tests."""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.new_record()
