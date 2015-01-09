import re
import os
import json
auto_prefix = u'\u200B'
path = "/home/snehasish/log/search1"
path = "/home/snehasish/log/search2"
for path, dirs, files in os.walk(path):
        for data in files:
                with open("/home/snehasish/log/search1/"+data) as text:
                        for line in text:
                                file1 = json.loads(line)
                                try:
                                        query = (file1["appData"]["_request_params"]["params"]["q"])[0]
                                        if auto_prefix in query:
                                                query = query.replace(auto_prefix, "")
                                                print file1["requestDate"],"-",query.encode('utf-8'), "- TRUE"
                                        else:
                                                print file1["requestDate"],"-",query.encode('utf-8'), "- FALSE"
                                except KeyError:
                                        pass
for path, dirs, files in os.walk(path):
        for data in files:
                with open("/home/snehasish/log/search2/"+data) as text:
                        for line in text:
                                file1 = json.loads(line)
                                try:
                                        query = (file1["appData"]["_request_params"]["params"]["q"])[0]
                                        if auto_prefix in query:
                                                query = query.replace(auto_prefix, "")
                                                print file1["requestDate"],"-",query.encode('utf-8'), "- TRUE"
                                        else:
                                                print file1["requestDate"],"-",query.encode('utf-8'), "- FALSE"
                                except KeyError:
                                        pass

