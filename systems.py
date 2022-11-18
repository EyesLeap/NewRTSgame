from System import System

class CombatSystem(System):
    '''
    >> from Entity import Entity
    >> from Component import Component
    >> from components import Damage, Health
    >> player = Entity('player')
    >> player.health = Health()
    >> player.damage = Damage()


    >> skeleton = Entity('skeleton')
    >> skeleton.health = Health()
    >> skeleton.damage = Damage()

    >> combat_sys = CombatSystem()
    >> combat_sys.update()
    '''
    components = ['Health', 'Damage']

    def update(self, dt=None):
        '''Updates the relevant data'''
        super(CombatSystem, self).update(dt=dt)
        entityA, entityB = self.entities
        #entityA.health.current_health -= entityB.damage()

