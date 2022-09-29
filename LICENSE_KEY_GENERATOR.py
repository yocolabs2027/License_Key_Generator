import os
import json
from github import Github

g = Github("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")
repo = g.get_user().get_repo("License-Key-Repo")
content = repo.get_contents("samp_keys.json")
decoded_content = content.decoded_content.decode()
result = json.loads(decoded_content)

file_name = 'test.json'
global data

class license_key:
    def __int__(self):
        pass
    def is_file_empty(self,file_name):
        global data
        return os.path.isfile(file_name) and os.path.getsize(file_name) == 0

    def licence_test(self):
        self.file_path = r'D:\license_key_generator\test.json'
        is_empty = self.is_file_empty(self.file_path)

        if is_empty:  ## If the JSON file is empty
            with open('test.json', 'w') as file:
                user_key = input('Enter Key')
                json.dump(user_key, file)
                print("Key added to the JSON file")
        else:
            ff = open('test.json', "r")
            data = json.loads(ff.read())
            if data in result.values():
                print("ACCESS GRANTED")

            while data not in result.values():
                print("NO ACCESS")
                with open('test.json','w') as filee:
                    user_key1 = input('Enter a valid Key')
                    json.dump(user_key1, filee)
                    if user_key1 in result.values():
                        print("ACCESS GRANTED")
                        break
if __name__ == "__main__":
    license_key().licence_test()