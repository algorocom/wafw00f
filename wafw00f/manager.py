#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

import os
from functools import partial
from pluginbase import PluginBase

def load_plugins():
    here = os.path.abspath(os.path.dirname(__file__))
    get_path = partial(os.path.join, here)
    plugin_dir = get_path('plugins')

    searchpath = [plugin_dir]
    if os.environ.get('WAFW00F_PLUGIN_DIR'):
        searchpath.append(os.environ.get('WAFW00F_PLUGIN_DIR'))

    plugin_base = PluginBase(
        package='wafw00f.plugins', searchpath=[plugin_dir]
    )
    plugin_source = plugin_base.make_plugin_source(
        searchpath=searchpath, persist=True
    )

    plugin_dict = {}
    for plugin_name in plugin_source.list_plugins():
        plugin_dict[plugin_name] = plugin_source.load_plugin(plugin_name)

    return plugin_dict
