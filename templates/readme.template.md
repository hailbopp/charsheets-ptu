<!--
Expects an object of this form:
{
    characters: [
        {
            name: "CharName",
            pokemon: [
                "pokename",
                "poke2 name"
            ]
        },
        ...
    ]
}
-->
# PTU Campaign Character Sheets

{% for character in characters %}
## {{character.name}}
[{{character.name}}'s sheet](md/{{character.name}}/character_sheet.md)

#### {{character.name}}'s Pokemon
{% for pokemon in character.pokemon %}
[{{pokemon}}](md/{{character.name}}/{{pokemon}}.md)
{% endfor %}
{% endfor %}
