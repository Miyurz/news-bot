
import simplejson as json
import requests
import sys
import time
import pycurl
import certifi
from io import BytesIO
#from termcolor import colored

def callRequest():
    #curl -H "X-Api-Key:  29631ea77aa84f768932119e3e7056d6" --request GET "https://newsapi.org/v2/top-headlines?country=in&category=business"
    #curl -H "Authorization: Basic 29631ea77aa84f768932119e3e7056d6" --request GET "https://newsapi.org/v2/top-headlines?country=in&category=business"
    #curl --request GET "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=29631ea77aa84f768932119e3e7056d6"
    
    print("HTTP request via {}".format(method))
    url = 'https://newsapi.org/v2/'
    '''
    Endpoints available: top-headline,everything,sources 
    Read more @ https://newsapi.org/docs/endpoints
    default endpoint = top-headline
    '''
    endpoint = 'top-headlines'
    headers = {'X-Api-Key':  '29631ea77aa84f768932119e3e7056d6'}
    params = (
      #('sources', ''),
      #('q', ''),
      ('pageSize', '99'),
      #('page', ''),
      ('country', 'in'),
      ('category', 'business'),
    )  
    response = requests.get('https://newsapi.org/v2/'+endpoint, headers=headers, params=params) 
    #print(response)
   
    # Ternary with raise https://stackoverflow.com/questions/10295841/raise-statement-on-a-conditional-expression
    #raise CustomException("Yikes! I got reponse code "+str(response.status_code))  if response.status_code != requests.codes.ok else print("OK") 
    if response.status_code != requests.codes.ok:
        raise Exception("ERROR: Got reponse code "+str(response.status_code))

    #builtin JSON decoder with requests
    #r = response.json()
    #print(r['totalResults'])

    #For better performance and if the number of network calls increase , consider moving to pycurl
    #https://stackoverflow.com/questions/15461995/python-requests-vs-pycurl-performance
    return response.text

def callPycurl():
   
    print("HTTP request via {}".format(method))
    
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

    #response = buffer.getvalue()
    #print(type(response))
    #print(response)
    return buffer.getvalue()

def getNews(response):
    
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

if __name__ == "__main__":
    print(sys.argv[1]);
    method = sys.argv[1]

    if method == "request":
        response = callRequest()
    elif method == "pycurl":
        response = callPycurl()
    else:
        print("ERROR: Unknown approach")
        sys.exit(1)
