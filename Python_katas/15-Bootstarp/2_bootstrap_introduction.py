"""Topic 2: Bootstrap Part 1 - Introduction To Bootstrap

Notes and small snippets about what Bootstrap is and how to use its CDN.
"""

BOOTSTRAP_CDN_LINK = (
    "<link rel=\"stylesheet\" "
    "href=\"https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css\">"
)

EXAMPLE_BASIC_PAGE = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Bootstrap Intro</title>
    {BOOTSTRAP_CDN_LINK}
  </head>
  <body>
    <h1 class="text-center text-primary">Hello Bootstrap</h1>
  </body>
</html>
"""
