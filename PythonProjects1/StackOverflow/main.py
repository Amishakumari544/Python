import shlex
import requests
from subprocess import Popen, PIPE
import os

def execute_and_return(cmd):
    print(cmd)
    args = shlex.split(cmd)
    proc = Popen(args, stdout=PIPE, stderr=PIPE)
    out,err = proc.communicate()
    return out, err

print(execute_and_return("C:/Program Files/AdoptOpenJDK/jdk-11.0.10.9-hotspot/bin/javac test.java"))

def make_request(error):
    print("Searching for "+error)
    resp  = requests.get("https://api.stackexchange.com/"+"2.2/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(error))
# resp  = requests.get("https://api.stackexchange.com/" +
#                         "/2.2/search?order=desc&sort=activity&tagged=c++&intitle={}&site=stackoverflow".format(error))
# resp  = requests.get("https://api.stackexchange.com/" +
#                     "/2.2/search?order=desc&sort=activity&tagged=java&intitle={}&site=stackoverflow.format(error))




def get_urls(json_dict):
    url_list = []
    count = 0
    for i in json_dict['items']:
        if i["is_answered"]:
            url_list.append(i["link"])
        count+=1
        if count == len(i) or count == 3:
            break
    import webbrowser
    for i in url_list:
        webbrowser.open(i)

if __name__ == "__main__":
    out, err = execute_and_return("javac test.java")
    # for python file---------- 
    # if err:
        # error_message = err.decode("utf-8").strip().split("\r\n")[-1]
    # ___________-------

    # for c++ file ------
    if err:
        error_message = err.decode("utf-8").strip().split("\r\n")[-1]
        # error_message = err.decode("utf-8").strip()
    else:
        error_message = err.decode("utf-8").strip().split("\r\n")[0]
    # _____________ ----- 
    print(error_message)
    if error_message:
        filter_out = error_message.split(":")
        print(filter_out)
        print(filter_out[0])
        json1 = make_request(filter_out[0])
        json2 = make_request(filter_out[1])
        json = make_request(error_message)
        get_urls(json1)
        get_urls(json2)
        get_urls(json)
    else:
        print("No errors")