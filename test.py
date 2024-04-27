from datetime import datetime
from service import Testservice
import time

def test():
    file = 'C:\\Users\\ANUPAMA\\Python\\log.txt'
    files = 'C:\\Users\\ANUPAMA\\Python\\test.txt'
    time=str(datetime.now())
    with open(files, 'a+') as f:
            f.write(f"service started at {time} ")

    while True:
        with open(file, 'a+') as f:
            f.write(str(datetime.now()))
        time.sleep(60)

class PythonService(Testservice):
    _svc_name_ = "PythonService"
    _svc_display_name_ = "TestPythonService"
    _svc_description_ = "Testing the window service"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        test()

if __name__ == '__main__':
    PythonService.parse_command_line()