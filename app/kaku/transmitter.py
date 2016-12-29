from time import sleep
import RPi.GPIO as GPIO


class Transmitter(object):
    """ Sends Kaku signal through 433Mhz transmitter """

    def __init__(self, gpio_pin):
        self.__pin = gpio_pin
        self.__repeats = 7
        self.__period = 260
        self.__pulse = 5

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.__pin, GPIO.OUT)
        GPIO.output(self.__pin, False)

        self.usleep = lambda x: sleep(x / 1000000.0)

    def transmit(self, packet):
        transmit = {
            '0': self.__transmit_low_bit,
            '1': self.__transmit_high_bit
        }

        for i in range(0, self.__repeats):
            self.__transmit_start()

            for c in packet:
                transmit.get(c)()

            self.__transmit_stop()

    def __transmit_high_bit(self):
        GPIO.output(self.__pin, True)
        self.usleep(self.__period)
        GPIO.output(self.__pin, False)
        self.usleep(self.__period * self.__pulse)
        GPIO.output(self.__pin, True)
        self.usleep(self.__period)
        GPIO.output(self.__pin, False)
        self.usleep(self.__period)

    def __transmit_low_bit(self):
        GPIO.output(self.__pin, True)
        self.usleep(self.__period)
        GPIO.output(self.__pin, False)
        self.usleep(self.__period)
        GPIO.output(self.__pin, True)
        self.usleep(self.__period)
        GPIO.output(self.__pin, False)
        self.usleep(self.__period * self.__pulse)

    def __transmit_start(self):
        """Send kaku start command """
        GPIO.output(self.__pin, True)
        self.usleep(self.__period)
        GPIO.output(self.__pin, False)
        self.usleep(self.__period * 10 + (self.__period >> 1))

    def __transmit_stop(self):
        """ Send kaku stop command """
        GPIO.output(self.__pin, True)
        self.usleep(self.__period)
        GPIO.output(self.__pin, False)
        self.usleep(self.__period * 40)
