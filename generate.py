import shutil
from os import listdir, makedirs
from os.path import isdir, join, exists

from jinja2 import Environment, FileSystemLoader
import yaml

jinja = Environment(
    loader=FileSystemLoader('./templates'),
)


def generate():
    if exists('md'):
        shutil.rmtree('md')
    makedirs('md')

    readme_template = jinja.get_template("readme.template.md")
    char_template = jinja.get_template("character.template.md")
    poke_template = jinja.get_template("pokemon.template.md")

    character_data = []
    characters = [d for d in listdir('characters') if isdir(join('characters', d))]
    for char_name in characters:
        with open('characters/%s/character.yml' % char_name, 'r') as sf:
            chardata = yaml.load(sf)
        char_result = char_template.render(chardata)
        makedirs('md/%s' % char_name)
        with open('md/%s/character_sheet.md' % char_name, 'w') as dest:
            dest.write(char_result)

        pokemon = [y for y in listdir('characters/%s/pokemon' % char_name)]
        for p in pokemon:
            with open('characters/%s/pokemon/%s' % (char_name, p), 'r') as poke_src:
                pokedata = yaml.load(poke_src)
            poke_result = poke_template.render(pokedata)
            with open('md/%s/%s.md' % (char_name, pokedata['name']), 'w') as dest:
                dest.write(poke_result)
        character_data.append({
            'name': char_name,
            'pokemon': [p.replace(".yml", "") for p in pokemon]
        })

    readme_str = readme_template.render({'characters': character_data})
    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_str)


if __name__ == "__main__":
    generate()
