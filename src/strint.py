
class Strint:
	def __init__(self):
		self.value = "0"
	def set(self,value):
		self.value = value
	def get(self):
		return self.value
	def increment(self):
		loop = {'0':'1','1':'2','2':'3','3':'4','4':'5','5':'6','6':'7','7':'8','8':'9','9':'0'}
		i = len(self.value)-1
		self.value = self.value[0:i] + loop[self.value[i]] + self.value[i+1:]
		while self.value[i] == '0':
			i -= 1
			if i < 0:
				self.value = "1" + self.value
				break
			self.value = self.value[0:i] + loop[self.value[i]] + self.value[i+1:]
	def decrement(self):
		loop = {'0':'9','1':'0','2':'1','3':'2','4':'3','5':'4','6':'5','7':'6','8':'7','9':'8'}
		i = len(self.value)-1
		self.value = self.value[0:i] + loop[self.value[i]] + self.value[i+1:]
		while self.value[i] == '9':
			i -= 1
			if i < 0:
				self.value = "0"
				break
			self.value = self.value[0:i] + loop[self.value[i]] + self.value[i+1:]
		if self.value[0] == '0' and len(self.value)>1:
			self.value = self.value[1:]
	def is_zero(self):
		return self.value == "0"
