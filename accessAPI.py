import requests
import json

print("Welcome to the Book of Mormon Summary Tool!")
while True:
  book = input("Which book of the Book of Mormon would you like?")
  chapter = input("Which chapter of {book} are you interested in?")

  base_url = f'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/{book}/{chapter}'

  response = requests.get(url)
  data = response.json()
  print("Summary of {book} chapter {chapter}:" + data['chapter']['summary'],"\n")
  if input("Would you like to view another (Y/N)?") != Y:
    print("Thank you for using the Book of Mormon Summary Tool!")
    break

