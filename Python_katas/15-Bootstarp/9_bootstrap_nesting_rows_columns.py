"""Topic 9: Bootstrap Part 8 - Nesting of Rows & Columns

Putting rows inside columns to create more complex layouts.
"""

NESTED_GRID_EXAMPLE = """<div class="container">
  <div class="row">
    <div class="col-md-8">
      Level 1: .col-md-8
      <div class="row">
        <div class="col-6">Nested col-6</div>
        <div class="col-6">Nested col-6</div>
      </div>
    </div>
    <div class="col-md-4">
      Sidebar
    </div>
  </div>
</div>
"""
