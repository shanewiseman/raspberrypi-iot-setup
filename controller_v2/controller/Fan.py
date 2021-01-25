import RPi.GPIO as gpio
from enum import Enum
import time
import datetime


class Fan():
    class Speed(Enum):
        HIGH = "HIGH"
        LOW = "LOW"
        OFF = "OFF"


    def __init__(self, low_pin, high_pin):
        self.low_pin = low_pin
        self.high_pin = high_pin
        self.mode = Fan.Speed.OFF

        self.__kill_theads = False

        gpio.setup(self.high_pin, gpio.OUT)
        gpio.setup(self.low_pin, gpio.OUT)
        
        self._on_flag = False
        self._off_flag = False
        self.control_thread = threading.Thread(target=self.__control, args=(), daemon=True)

        self.hardware_thread = threading.Thread(target=self.__hardware, args=(), daemon=True)

        self.message_thread = threading.Thread(target=self.__message, args=(), daemon=True)

        self.control_thread.start()
        self.message_thread.start()

    def on(self):
        self._off_flag = False
        self._on_flag = True
    def off(self):
        self._on_flag = False
        self._off_flag = True


    def __control(self):

        self.stop_thread = None
        self.__stop_stop_thread = False
        while self.__kill_threads is False:
            if self._on_flag:
                if self.stop_thread is not None and self.stop_thread.is_alive():
                    self.__stop_stop_thread = True
                    self.stop_thread.join()
                    self.__stop_stop_thread = False
                
                c_time = datetime.datetime.now.time()
                if datetime.time(9,0) >= c_time or datetime.time(18,0) <= c_time:
                    self.mode = Fan.Speed.HIGH
                else:
                    self.mode = Fan.Speed.LOW

            if self._off_flag and self.stop_thread is None:
                self.on_time_length = 30
                self.stop_thread = \
                        threading.Thread(target=self.__stop, args=(), daemon=True)
                self.stop_thread.start()


    def __stop(self):
        start_time = time.time()
        while ((time.time() - start_time) < (self.on_time_length * 60)) or \
                self.__stop_stop_thread or self__kill_threads:

            time.sleep(1)

        self.mode = Fan.Speed.OFF

    def __hardware(self):
        
        while self.__kill_threads is False:
            if self.mode == Fan.Speed.OFF:
                pass
            elif self.mode == Fan.Speed.HIGH:
                pass
            elif self.mode == Fan.Speed.LOW:
                pass

            time.sleep(1)

    def __message(self):
        pass





                
                




