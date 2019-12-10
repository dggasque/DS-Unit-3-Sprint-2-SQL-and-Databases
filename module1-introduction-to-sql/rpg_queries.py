import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

q1 = 'SELECT COUNT(character_id) FROM charactercreator_character;'

num_chars = curs.execute(q1).fetchall()

print(f'There are {num_chars[0][0]} Characters.')

q2 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_cleric'

num_clerics = curs.execute(q2).fetchall()

print(f'There are {num_clerics[0][0]} Characters of the class Cleric.')

q3 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_fighter'

num_fighter = curs.execute(q3).fetchall()

print(f'There are {num_fighter[0][0]} Characters of the class Fighter.')

q4 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_mage'

num_mage = curs.execute(q2).fetchall()

print(f'There are {num_mage[0][0]} Characters of the class Mage.')

q5 = 'SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer;'

num_necromancer = curs.execute(q5).fetchall()

print(f'There are {num_necromancer[0][0]} Characters of the Mage subclass Necromancer.')

q6 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_thief;'

num_theif = curs.execute(q6).fetchall()

print(f'There are {num_theif[0][0]} Characters of the class Thief.')

q7 = 'SELECT COUNT(item_id) FROM armory_item;'

num_items = curs.execute(q7).fetchall()

print(f'There are {num_items[0][0]} Items.')

q8 = 'Select COUNT(item_ptr_id) FROM armory_weapon;'

num_weapons = curs.execute(q8).fetchall()

print(f'There are {num_weapons[0][0]} Weapons.')

q9= """
    SELECT cc.character_id, cc.name, COUNT(cci.item_id)
    FROM charactercreator_character as cc,
    charactercreator_character_inventory as cci
    WHERE cc.character_id = cci.character_id
    GROUP BY cc.character_id
    LIMIT 20;
    """

print(curs.execute(q9).fetchall())

q10 = """
    SELECT cc.character_id, cc.name, COUNT(aw.item_ptr_id)
    FROM charactercreator_character as cc,
    armory_item as ai,
    armory_weapon as aw,
    charactercreator_character_inventory as cci
    WHERE cc.character_id = cci.character_id
    AND cci.item_id = ai.item_id
    AND ai.item_id = aw. item_ptr_id
    GROUP BY cc.character_id
    LIMIT 20;
    """

print(curs.execute(q10).fetchall())

q11 = """
    SELECT AVG(item_count)
    FROM
    (SELECT cc.character_id, cc.name, COUNT(cci.item_id) as item_count
    FROM charactercreator_character as cc,
    charactercreator_character_inventory as cci
    WHERE cc.character_id = cci.character_id
    GROUP BY cc.character_id);
    """
result = curs.execute(q11).fetchall()


print(f"The Characters have an average of {round(result[0][0], 3)} Items")

q12 = """
    SELECT AVG(weapon_count)
    FROM
    (SELECT cc.character_id, cc.name, COUNT(aw.item_ptr_id) as weapon_count
    FROM charactercreator_character as cc,
    armory_item as ai,
    armory_weapon as aw,
    charactercreator_character_inventory as cci
    WHERE cc.character_id = cci.character_id
    AND cci.item_id = ai.item_id
    AND ai.item_id = aw. item_ptr_id
    GROUP BY cc.character_id)
    ;
    """

result2 = curs.execute(q12).fetchall()

print(f"The Characters have an average of {round(result2[0][0], 3)} Weapons")
