from uuid import uuid4 as uuid
import pyqrcode
from collections import OrderedDict
import requests

def code():
	#__variable de ejemplo para los codigos
	ejemplo=uuid().hex[:15]

	code = pyqrcode.create(ejemplo)

	url = 'https://hci-server-uvg.herokuapp.com/machine/code'
	params = OrderedDict([('code', ejemplo), ('points', 10)])

	results = requests.post(url, data={'code': ejemplo, 'points':10})
	print(results)

	code.png('code.png', scale=8)
	f = open("code.txt", "r+")
	f.truncate(0)
	f.write(ejemplo)
	f.close()
	return ejemplo