# Copyright (c) 2015 Ultimaker B.V.
# Uranium is released under the terms of the AGPLv3 or higher.

from . import SimpleView

from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("uranium")

def getMetaData():
    return {
        "plugin": {
            "name": i18n_catalog.i18nc("@label", "Simple View"),
            "author": "Ultimaker",
            "version": "1.0",
            "decription": i18n_catalog.i18nc("@info:whatsthis", "Provides a simple solid mesh view."),
            "api": 2
        },
        "view": {
            "name": i18n_catalog.i18nc("@item:inmenu", "Simple")
        }
    }

def register(app):
    return { "view": SimpleView.SimpleView() }

