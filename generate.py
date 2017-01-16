from copy import deepcopy

import shutil
from docx import Document
from docxtpl import DocxTemplate, R
from os import listdir, makedirs
from os.path import isdir, join, exists

from jinja2 import Environment, FileSystemLoader
import yaml

jinja = Environment(
    loader=FileSystemLoader('./templates'),
)

characters = [d for d in listdir('characters') if isdir(join('characters', d))]
with open('data/movelist.yml') as movesfile:
    moves_data = yaml.load(movesfile)


def generate():
    if exists('md'):
        shutil.rmtree('md')
    makedirs('md')

    readme_template = jinja.get_template("readme.template.md")
    char_template = jinja.get_template("character.template.md")
    poke_template = jinja.get_template("pokemon.template.md")

    character_data = []
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


def get_movedata(move_name):
    for move in moves_data:
        if move['Name'] == move_name:
            return move


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def combine_word_documents(files, target):
    merged_document = Document()

    for index, file in enumerate(files):
        sub_doc = Document(file)

        # Don't add a page break if you've reached the last file.
        if index < len(files)-1:
            sub_doc.add_page_break()

        for element in sub_doc.element.body:
            merged_document.element.body.append(element)

    merged_document.save(target)


def generate_cards():
    if exists('cards'):
        shutil.rmtree('cards')
    makedirs('cards')

    moves = []
    for char_name in characters:
        with open('characters/%s/character.yml' % char_name, 'r') as sf:
            chardata = yaml.load(sf)
            for m in chardata['moves']:
                move = get_movedata(m)
                move['CharacterName'] = char_name
                moves += [move]
        pokemon = [y for y in listdir('characters/%s/pokemon' % char_name)]
        for p in pokemon:
            with open('characters/%s/pokemon/%s' % (char_name, p), 'r') as poke_src:
                pokedata = yaml.load(poke_src)
            for m in pokedata['moves']:
                try:
                    move = deepcopy(get_movedata(m))
                    move['CharacterName'] = R("%s (%s)\n%s" % (pokedata['name'], pokedata['species'], char_name))

                    # Apply STAB
                    if move['Type'] in pokedata['types'] and move.get('Damage', None):
                        move['Damage'] = int(move['Damage']) + 2
                    if move.get('Damage', None):
                        move['Damage'] = "DB " + str(move['Damage'])
                    moves += [move]
                except Exception as e:
                    print(e)
                    print(m)

    docnum = 0
    pages = list(chunks(moves, 5))
    for card_page in pages:
        print(card_page)
        while len(card_page) < 5:
            card_page += [{}]
        movecard_template = DocxTemplate("templates/movecards.template.docx")
        movecard_template.render({'moves': card_page})
        movecard_template.save('cards/cards_%d.docx' % docnum)
        docnum += 1

    #doc_files = ['cards/cards_%d.docx' % n for n in range(len(pages))]
    #combine_word_documents(doc_files, "cards/cards.docx")


if __name__ == "__main__":
    generate()
    generate_cards()
