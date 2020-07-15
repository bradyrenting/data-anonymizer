from ruamel.yaml import YAML


class config:
    def __init__(self, fileobject):
        self.fileobject = fileobject
        self.yaml = YAML(typ='safe')
        self.yamlconfig = self.yaml.load(fileobject)

    def storage(self):
        return self.yamlconfig['storage']

    def tables(self):
        return self.yamlconfig['anonymize']

    def columns(self, table):
        return self.tables()[table]['columns']

    def iterator(self, table):
        return self.tables()[table]['iterator']['name']


# Testing
if __name__ == "__main__":
    c = config(open('config.yml', 'r'))

    print(c.storage()['host'])
    print(c.storage()['username'])
    print(c.storage()['password'])
    print(c.storage()['database'])

    for table in c.tables():
        print(table)
        for column in c.columns(table):
            print(column + ' ' + str(c.columns(table)[column]))
