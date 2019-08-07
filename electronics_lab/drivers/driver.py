import visa


class Driver:

    def __init__(self, resource_string, debug=False):
        resources = visa.ResourceManager()
        self.instrument = resources.open_resource(resource_string)
        self.debug = debug

    def print_info(self):
        self.instrument.write('*IDN?')
        fullreading = self.instrument.read_raw()
        readinglines = fullreading.splitlines()
        print("Instrument information: " + readinglines[0])

    class Measurement:
        def __init__(self, name='', description='', command='', unit='', return_type=''):
            self.name = name
            self.description = description
            self.command = command
            self.unit = unit
            self.return_type = return_type
