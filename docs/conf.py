# Copyright 2024 Remy Blank <remy@c-space.org>
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

from tdoc.common.defaults import *
from tdoc.common.wsgi import hostname_re

project = "t-doc.org"
author = "Remy Blank"
license = 'CC-BY-NC-SA-4.0'
language = 'fr'

# myst_links_external_new_tab = True

html_logo = 'logo.svg'
html_css_files = ['site-styles.css']
html_theme_options = {
    'repository_url': 'https://github.com/t-doc-org/t-doc-org.github.io',
}

# Serve as domain storage.
tdoc_domain_storage = {
    **tdoc_domain_storage,
    'allowed_origins': rf'^https://(?:{hostname_re}\.)?t-doc\.org$',
    'allowed_keys': '^tdoc:domain:.*$',
}
