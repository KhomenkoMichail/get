import smbus
import time

class MCP3021:
    def __init__(self, drange, verbose = False):
        self.bus = smbus.SMBus(1)
        self.drange = drange
        self.address = 0x4D
        self.verbose = verbose
    
    def deinit(self):
        self.bus.close()
    
    def get_num(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_byte_data = data >> 8
        upper_byte_data = data & 0xFF
        number = (upper_byte_data << 6) | (lower_byte_data >> 2)
        if self.verbose:
            print(f"Accepted data: {data}, High: {upper_byte_data:x}, Low: {lower_byte_data:x}, Num: {number}\n")
        return number
    
    def get_vol(self):
        return self.drange * self.get_num() / 1024


if __name__ == "__main__":
    try:
        mcp = MCP3021(5.15)
        
        while True:
            print(f"Voltage is: {mcp.get_vol()}")
            time.sleep(0.3)
    finally:
        mcp.deinit()