import spidev

def readADC(channel=0, device=0):
	bus = 0
	
	spi = spidev.SpiDev()
	spi.open(bus, device)
	spi.max_speed_hz = int(1e6)
	
	config = [0b01101000, 0] if channel == 0 else [0b01111000, 0]
	byt = spi.xfer2(config)
	data = (byt[0] << 8) | byt[1]
	
	spi.close()
	return data * 3.3 / 1023
