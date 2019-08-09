from .driver import Driver


class SiglentSDM3055(Driver):
    dc_voltage = Driver.Measurement(name='dc_voltage', command='DC', unit='Volts', return_type='float',
                                    description='DC voltage value')
    ac_voltage = Driver.Measurement(name='ac_voltage', command='AC', unit='Volts', return_type='float',
                                    description='AC voltage value')
    dc_current = Driver.Measurement(name='dc_current', command='DC', unit='Amperes', return_type='float',
                                    description='DC current value')
    ac_current = Driver.Measurement(name='ac_current', command='AC', unit='Amperes', return_type='float',
                                    description='AC current value')
    capacitance = Driver.Measurement(name='capacitance', command='CAP', unit='Farads', return_type='float',
                                     description='Measures capacitance')
    twow_resistance = Driver.Measurement(name='twow_resistance', command='RES', unit='Ohms', return_type='float',
                                         description='Two wire resistance in Ohms')
    frequency = Driver.Measurement(name='frequency', command='FREQ', unit='Hz', return_type='float',
                                   description='Signal frequency in Hz')
    period = Driver.Measurement(name='period', command='PER', unit='Seconds', return_type='float',
                                description='Signal period in seconds')

    def get_measurement(self, meas_type=dc_voltage):

        if meas_type.unit == 'Volts':
            reading = float(self.instrument.query('MEAS:VOLT:{}?'.format(meas_type.command)))
            print(" value is " + str(reading) + " " + meas_type.unit)

        if meas_type.unit == 'Amperes':
            reading = float(self.instrument.query('MEAS:CURR?'.format(meas_type.command)))
            print(" value is " + str(reading) + " " + meas_type.unit)

        if meas_type.unit == 'Farads':
            reading = float(self.instrument.query('MEAS:CAP?'))
            print(" value is " + str(reading) + " " + meas_type.unit)

        if meas_type.unit == 'Ohms':
            if meas_type.name == 'twow_resistance':
                reading = float(self.instrument.query('MEAS:RES?'))
                print(" value is " + str(reading) + " " + meas_type.unit)

        if meas_type.unit == 'Hz':
            reading = float(self.instrument.query('MEAS:FREQ?'))
            print(" value is " + str(reading) + " " + meas_type.unit)

        if meas_type.unit == 'Seconds':
            reading = float(self.instrument.query('MEAS:PER?'))
            print(" value is " + str(reading) + " " + meas_type.unit)

        return reading
