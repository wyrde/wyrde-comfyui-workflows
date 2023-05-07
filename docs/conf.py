# conf.py
# https://docs.readthedocs.io/en/stable/config-file/v2.html
# https://docs.readthedocs.io/en/stable/guides/migrate-rest-myst.html

source_suffix = [
    ".md",
    ".rst",
]

extensions = [
    # Your existing extensions
    "myst_parser",
]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "substitution"
]
