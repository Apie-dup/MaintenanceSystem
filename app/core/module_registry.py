class ModuleRegistry:

    def __init__(self):

        self.module = {}

    def register(self, name, page_name):

        self.module[name] = page_name

    def get(self, name)
        
        return self.module.get(name)
    
    def name(self):

        return list(self.module.keys())