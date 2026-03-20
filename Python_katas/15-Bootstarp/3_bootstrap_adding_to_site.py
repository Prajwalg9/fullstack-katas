"""Topic 3: Bootstrap Part 2 - Adding Bootstrap To Our Site

Practice adding Bootstrap CSS/JS to Django templates or plain HTML files.
"""

BOOTSTRAP_JS_BUNDLE = (
    "<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js\"></script>"
)

def get_bootstrap_base_template():
    """Return a minimal Django base template string with Bootstrap included."""
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{{% block title %}}My Site{{% endblock %}}</title>
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
  </head>
  <body>
    <div class="container">
      {{% block content %}}{{% endblock %}}
    </div>
    {BOOTSTRAP_JS_BUNDLE}
  </body>
</html>
"""
