#!/usr/bin/env python3
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
	'''This function takes in a url, downloads the data from the url, turning it into a JSON string, finally converting it into a python list/dict.'''
	json_temp = requests.get(url).text
	python_product = json.loads(json_temp)
	return python_product

def print_events(events, n=5):
	'''Loops over first n items in events, prints each item in form type::repo'''
	for x in events[:n]:
    		event = x['type'] + ' :: ' + x['repo']['name']
    		print(event)

def main():
	'''prints values of GHUSER, url, retrieve_events, and print_events'''
	print(GHUSER)
	print(url)
	events = retrieve_events(url)
	print_events(events)

if __name__ == "__main__":
	main()
	
