import json

from collections import OrderedDict as dict
class Component:
    '''Contains a set of unique properties or attributes that can be
    associated with an Entity

    Components have a tightly coupled relationship with an entity
    '''
    __slots__ = ['defaults', 'entity']
    #defaults = dict()
    Catalog = dict()
    ComponentTypes = dict()

    def __init__(self, entity=None, **properties):
        '''properties'''
        self.entity = entity
        for prop, val in self.defaults.items():
            setattr(self,prop, properties.get(prop,val))
    '''
    def __new__(cls, entity=None, **properties):
        cname = cls.__name__
        if cname not in Component.ComponentTypes:
            Component.ComponentTypes[cname] = cls
            cls.Catalog = dict()
        if entity not in cls.Catalog:
#            component = super(Component, cls).__new__(cls, entity=entity, **properties)
            pass
        else:
            component = cls.Catalog(entity)
        return component
    '''
    def __repr__(self):
        '''<Component entity_id>'''
        cname = self.__class__.__name__
        entity_name = ''
        if self.entity:
            for prop_name, component in self.entity.components.items():
                if component == self:
                    entity_name = ' entity:{}.{}'.format(self.entity.name, prop_name)
                    break
        return '<{}{}>'.format(cname, entity_name)


    def __str__(self):
        '''Dump out the JSON of the properties'''
        keys = self.defaults.keys()
        data = dict()
        for key in keys:
            if key != 'defaults':
                data[key] = getattr(self, key)
        json_string = '\n'.join(
            line.rstrip()
            for line in json.dumps(data, indent=4).split('\n')
        )
        return json_string
    def __getitem__(self, key):
        '''Allows to attributes as a dictionary'''
        return getattr(self, key)
    def __setitem__(self, key, value):
        return setattr(self,key,value)

    def restart(self):
        for prop_name, value in self.defaults.items():
            setattr(self, prop_name,value)



