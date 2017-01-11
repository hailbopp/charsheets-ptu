# {{name}}
------------------------------------------------------------------------

### Overview
Level {{level}} {{gender|lower}} {{nature}} {{species}}
{% if (types|length) is equalto 2 -%}
Type: {{types|first}} / {{types|last}}
{% else -%}
Type: {{types|first}}
{% endif -%}
Height: {{height}}
Weight: {{weight}}
{{level + (stats.hp * 3) + 10}} HP

### Basic Stats
| Stat              | Value |
| ----------------- | ----- |
| HP                | {{stats.hp}} |
| Attack            | {{stats.attack}} |
| Special Attack    | {{stats.special_attack}} |
| Defense           | {{stats.defense}} |
| Special Defense   | {{stats.special_defense}} |
| Speed             | {{stats.speed}} |

### Abilities
{% for ability in abilities -%}
* {{ability}}
{% endfor %}
### Capabilities
| Capability    | Value |
| ------------- | ----- |
{% for name, value in capabilities.items()|sort -%}
| {{name}} | {{value|default('', True)}} |
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
### Advancement
Tutor Points: {{tutor_points}}
XP: {{current_xp}}

