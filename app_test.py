import requests, json

def get_test(id):
	r = requests.get('http://localhost:8080/task/%d' % id)
	print r.json()

def post_test():
	
	payload = {'title': 'task 2'}
 	r = requests.post("http://localhost:8080/task", data=payload)
 	print r.content


def main():
	get_test(4)
	#post_test()

if __name__ == '__main__':
	main()