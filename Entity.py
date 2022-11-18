from uuid import uuid4
from collections import OrderedDict as dict
from Component import Component
class Entity:

    __slots__ = ['uid', 'name', 'components']

    def __init__(self, name=None, uid=None):
        self.uid = uuid4() if uid is None else uid
        self.name = name or ''
        self.components = dict()

    def __repr__(self):
        '''<Entity enemy:0'''
        cname = self.__class__.__name__
        name = self.name or self.uid
        if name != self.uid:
            name = '{}:{}'.format(name, self.uid)
        return '<{} {}>'.format(cname, name)
    def __str__(self):
        '''{collection of the components here}'''
        return str(self.components)
    def __getitem__(self, key):
        '''Returns the component value using the key'''
        return self.components[key]
    def __setitem__(self, key, value):
        '''Sets the component using the key and value'''

        #TODO: Component updates
        self.components[key] = value
    def __getattr__(self, key):
        '''Allows access to the properties/components as an attribute'''
        if key in super(Entity, self).__getattribute__('__slots__'):
            return super(Entity, self).__getattr__(key)
        else:
            return self.components[key]

    def __setattr__(self, key, value):
        '''Allows access to the properties/components as an attribute'''
        if key in super(Entity, self).__getattribute__('__slots__'):
            super(Entity, self).__setattr__(key, value)
        else:
            #TODO: Add component logic
            if isinstance(value, Component):
                vCatalog = value.__class__.Catalog
                if value.entity is None:
                    value.entity = self
                    for entity, comp in vCatalog.items():
                        if comp == value:
                            if entity not in vCatalog:
                                vCatalog.pop(entity)
                                for relationship_name, component in entity.components:
                                    if component == value:
                                        entity.components.pop(relationship_name)
                                        break
                            vCatalog[self] = value

            self.components[key] = value
