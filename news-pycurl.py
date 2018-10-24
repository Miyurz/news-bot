
import simplejson as json
import pycurl
import sys
import time
import certifi
from io import BytesIO


#from termcolor import colored

def getNews():
    #curl -H "X-Api-Key:  29631ea77aa84f768932119e3e7056d6" --request GET "https://newsapi.org/v2/top-headlines?country=in&category=business"
    #curl -H "Authorization: Basic 29631ea77aa84f768932119e3e7056d6" --request GET "https://newsapi.org/v2/top-headlines?country=in&category=business"
    #curl --request GET "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=29631ea77aa84f768932119e3e7056d6"
    
    buffer = BytesIO()
    url = 'https://newsapi.org/v2/'
    '''
    Endpoints available: top-headline,everything,sources 
    Read more @ https://newsapi.org/docs/endpoints
    default endpoint = top-headline
    '''
    endpoint = 'top-headlines'
    
    headers = "X-Api-Key:  29631ea77aa84f768932119e3e7056d6"
    params = "?country=in&category=business&pageSize=99"
    r = pycurl.Curl()
    r.setopt(r.URL, url+endpoint+params)
    r.setopt(r.HTTPHEADER, [headers] )
    r.setopt(r.WRITEDATA, buffer)
    r.setopt(r.CAINFO, certifi.where())
    r.perform()
    r.close()

    response = buffer.getvalue()
    #print(type(response))
    #print(response)
    
    #Decode json
    try:
        parsedJson = json.loads(response)
    except ValueError:
        raise('Decoding JSON has failed')
    else:
        #print("parsedJson is dictionary", parsedJson)
        #count = sum(len(v)for v in parsedJson.values())
        parseJson(parsedJson)
    finally:
        print("Executing cleanup!")
    
def parseJson(parsedJson):
    for key, value in parsedJson.items():
        if key == "articles":

            #print("Type: parsedJson2 = "+str(type(parsedJson2)))
            #print("Type: key = "+str(type(key)))
            #print("Type: value = "+str(type(value)))
            #print("Type: parsedJson = "+str(type(parsedJson)))
            for item in value:
                print("Type: item = {}".format(type(item)))
                print('*' * 40)
                #print('{} '.format(**item))

                for k, v in item.items():
                    #Display with a pause to let user read
                    if k == "source":
                        print("Type: source = {}".format(type(k)))
                    else:
                        print("{} : {}".format(k, v))
                #time.sleep(1)
                       
getNews()
