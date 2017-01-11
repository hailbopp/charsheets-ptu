# {{name}}
------------------------------------------------------------------------

### Overview
{{age}}-year-old {{gender|lower}} {{background.name}}
Level {{level}}
{{ (level * 2) + (stats.hp * 3) + 10 }} HP
{{ ((level / 5)|int) + 5 }} AP

### Basic Stats
| Stat              | Value |
| ----------------- | ----- |
| HP                | {{stats.hp}} |
| Attack            | {{stats.attack}} |
| Special Attack    | {{stats.special_attack}} |
| Defense           | {{stats.defense}} |
| Special Defense   | {{stats.special_defense}} |
| Speed             | {{stats.speed}} |

### Features
{% for feature in features -%}
* {{feature}}
{% endfor %}
### Edges
{% for edge in edges -%}
* {{edge}}
{% endfor %}
### Actions
{% for action in actions -%}
* {{action}}
{% endfor %}
### Moves
{% for move in moves -%}
* {{move}}
{% endfor %}
### Skills
| Skill         | Rank |
| ------------- | ---- |
{% for skill, rank in skills.items()|sort -%}
| {{skill}} | {{rank}} |
{% endfor %}
{% if capabilities -%}
### Capabilities
| Capability    | Value |
| ------------- | ----- |
{% for name, value in capabilities.items()|sort -%}
| {{name}} | {{value|default('', True)}} |
{% endfor %}
{% endif -%}
### Equipment
| Slot          | Item |
| ------------- | ---- |
{% for slot, item in equipment.items()|sort -%}
| {{slot}} | {{item|default("empty", True)}} |
{% endfor %}
### Inventory
| Item          | Quantity |
| ------------- | -------- |
{% for item, quantity in inventory.items()|sort -%}
| {{item}} | {{quantity}} |
{% endfor %}
### Advancement
Level {{level}}
Current XP: {{current_xp}} / 10
