import eel
import random

eel.init('web')


@eel.expose
def get_random_number():
    eel.editValue(random.randint(1, 100))


eel.start('index.html')
