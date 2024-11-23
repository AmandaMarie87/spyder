# -*- coding: utf-8 -*-
#
# Copyright © Spyder Project Contributors
# Licensed under the terms of the MIT License
# (see spyder/__init__.py for details)

"""Shortcuts utils."""

from dataclasses import dataclass
from typing import Optional

from qtpy.QtCore import QObject


@dataclass(frozen=True)
class ShortcutData:
    """Dataclass to represent shortcut data."""

    qobject: QObject
    """QObject to which the shortcut will be associated."""

    name: str
    """Shortcut name (e.g. "run cell")."""

    context: str
    """
    Name of the shortcut context.

    Notes
    -----
    This can be the plugin name (e.g. "editor" for shortcuts that have
    effect when the Editor is focused) or "_" for global shortcuts.
    """

    plugin_name: Optional[str] = None
    """
    Name of the plugin where the shortcut is defined.

    Notes
    -----
    This is only necessary for third-party plugins that have shortcuts with
    several contexts.
    """

    add_shortcut_to_tip: bool = False
    """Whether to add the shortcut to the qobject's tooltip."""
