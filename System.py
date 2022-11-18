from Component import Component
class System:
    '''Identifies a set of components that need to be processed

    System has a loose coupling with Components and Entities

    >> from Entity import Entity
    >> from components import

    '''
    components = []
    Catalog = {}

    @property
    def entities(self):
        return list(set(entity for component_cls in self.component_classes
                       for entity in component_cls.Catalog.keys()
                       if entity is not None))
    @property
    def component_classes(self):
        return list(set(Component.ComponentTypes.get(component_name)
                        for component_name in self.components
                        if component_name in Component.ComponentTypes))


    def __new__(cls, name=None, components=[]):
        '''Adds systems to the catalog '''
        name = cls.__name__ if name is None else name
        if name not in System.Catalog:
            system = super(System, cls).__new__(cls, name=name, components=components)
            System.Catalog[name] = system


        else:
            system = System.Catalog[name]
        return system
    def __init__(self, name=None, components=[]):
        '''Initializes name and components '''
        self.name = name
        if components:
            self.components = components
    def __repr__(self):
        '''<System name>'''
        cname = self.__class__.__name__
        self.name = name
        return '<{} {}>'.format(cname, name)

    def update(self, dt=None):
        raise NotImplemented('not implemented...')
