import vxi11
from .driver import Driver


class SiglentSPD3303X(Driver):

    def __init__(self, ip_string, debug=False):
        self.instrument = vxi11.Instrument(ip_string)
        self.debug = debug

    def print_info(self):
        print("Instrument information: {}".format(self.instrument.ask("*IDN?")))

    voltage = Driver.Measurement(name='voltage', command='DC', unit='Volts', return_type='float',
                                 description='DC voltage value')
    current = Driver.Measurement(name='current', command='DC', unit='Amperes', return_type='float',
                                 description='DC current value')
    power = Driver.Measurement(name='power', command='DC', unit='Watts', return_type='float',
                               description='DC power value')
    out = Driver.Measurement(name='out', command='DC', unit=None, return_type='str',
                             description='channel ON or OFF')

    def get_measurement(self, channel=1, meas_type=voltage):

        if meas_type.unit == 'Volts':
            reading = float(self.instrument.ask('MEAS:VOLT? CH{}'.format(channel)))
            print("Channel " + str(channel) + " value is " + str(reading) + " " + meas_type.unit)

        if meas_type.unit == 'Amperes':
            reading = float(self.instrument.ask('MEAS:CURR? CH{}'.format(channel)))
            print("Channel " + str(channel) + " value is " + str(reading) + " " + meas_type.unit)

        if meas_type.unit == 'Watts':
            reading = float(self.instrument.ask('MEAS:POWE? CH{}'.format(channel)))
            print("Channel " + str(channel) + " value is " + str(reading) + " " + meas_type.unit)

        if meas_type.unit is None:
            reading = int(self.instrument.ask('SYST:STAT?'), 16)
            reading = str(format(reading, '10b'))
            if channel == 1:
                reading = str(reading[5])

            if channel == 2:
                reading = str(reading[6])

            if reading == '1':
                out = "ON"
            else:
                out = "OFF"
            print("Channel " + str(channel) + " is " + str(out) + " ")

            try:
                reading = int(reading)
            except TypeError:
                reading = None

        return reading

    def set_param(self, channel=1, param=voltage, value=0):

        if param.name == 'voltage':
            self.instrument.write('CH' + str(channel) + ':VOLT ' + str(value))
            print("Set Channel " + str(channel) + " value as " + str(value) + " " + param.unit)

        if param.name == 'current':
            self.instrument.write('CH' + str(channel) + ':CURR ' + str(value))
            print("Set Channel " + str(channel) + " value as " + str(value) + " " + param.unit)

        if param.unit is None:
            if value == 1 or value == '1' or value == 'ON':
                self.instrument.write('OUTP CH' + str(channel) + ',ON')
                print("Set Channel " + str(channel) + " state as ON ")
            elif value == 0 or value == '0' or value == 'OFF':
                self.instrument.write('OUTP CH' + str(channel) + ',OFF')
                print("Set Channel " + str(channel) + " state as OFF ")
            else:
                print("INVALID command")
