from collections import OrderedDict as dict
from Component import Component
from random import randint



class Health(Component):
    '''Contains current and max value of health for an entity

    >> from Entity import Entity
    >> player = Entity('player',0)
    >> player.health = Health(current_health=100,max_health=100)
    <Health player>
    >> print player.health
    {
        "current_health":100,
        "max_health": 100
    }
    >> print player.health.current_health
    100
    >> print player.health['current_health']
    100
    >> player.health['current_health'] = 50
    >> print player.health
    {
        "current": 50,
        "max_health": 100
    }
    '''
    defaults = dict()
    defaults['current_health'] = 100
    defaults['max_health'] = 100
    @property
    def alive(self):
        return self.current > 0
class Damage(Component):
    defaults = dict()
    defaults['min_damage'] = 10
    defaults['max_damage'] = 20

    def __call__(self):
        '''Returns a damage calculation based on the properties of the component
            player = Entity('player', 0)
            player.damage = Damage(entity=player, min_damage=15, max_damage=20)
            player.damage()

        '''
        total_damage = randint(self.defaults['min_damage'], self.defaults['max_damage'])

        return total_damage