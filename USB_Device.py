import usb.core
import sys

class Device:
	def find_correct_version(self, version):
		devs = usb.core.find(find_all=True)
		count = 0
		for d in devs:
			if d.idVendor == self.idVendor and d.idProduct == self.idProduct:
				if(count == version):
					self.dev = d
					break
				else:
					count+=1


	def initialize(self, version):
		self.find_correct_version(version)
		ep = self.dev[0].interfaces()[self.interface_index].endpoints()[self.endpoint_index]
		i = self.dev[0].interfaces()[self.interface_index].bInterfaceNumber
		self.dev.reset()

		if self.dev.is_kernel_driver_active(i):
			try:
				self.dev.detach_kernel_driver(i)
			except usb.core.USBError as e:
				sys.exit("Could not detach kernel driver from interface({0}): {1}".format(i, str(e)))

		self.eaddr = ep.bEndpointAddress


	def __init__(self, idVendor, idProduct, interface_index, endpoint_index, version=0):
		self.idVendor = idVendor
		self.idProduct = idProduct
		self.interface_index = interface_index
		self.endpoint_index = endpoint_index
		self.initialize(version)
	
	
	def get_device_readout(self):
		try:
			return self.dev.read(self.eaddr, 64, 10)
		except:
			return []
