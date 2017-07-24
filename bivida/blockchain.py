import requests
import blockchain


secret = 'ZzsMLGKe162CfA5EcG6j'

my_xpub = '6be4ea74-5eb4-4bca-bda4-576971a72938'
my_api_key ='b39c2481-3fa3-4722-a346-6f50c8b8275c'

my_callback_url = 'http://bivida.azurewebsites.net'

BASE_url = 'https://api.blockchain.info/v2/'

def recieve_info_wallet():
    request_url = (BASE_url + 'receive?xpub=%s&callback=%s&key=%s') % (my_xpub, my_callback_url, my_api_key)
    print 'GET request url : %s' % (request_url)
    wallet_info = requests.get(request_url).json()
    if wallet_info['id'] == 20:
        if len(wallet_info[id]):

            print 'Your Id is:- %s' % (wallet_info['id'])
            print 'Your Address is:- %s' % (wallet_info['aadr'])
            print 'Your Operation is' % (wallet_info['op'])
            print 'Your Callback URL is' % (wallet_info['callback'])
            print 'Your Notification is ' % (wallet_info['onNotification'])
        else:
            print 'You have invalid wallet.'
    else:
        # Here we are printing some line if we get some other meta code other than 200.
        print 'Your wallet have different Id other than 20'

def delete_the_request():
    request_url = (BASE_url + 'receive/block_notifcation/64?key=%s') % (my_api_key)
    print 'POST request url : %s' % (request_url)
    response = requests.post(request_url).json()
    if len(response['deleted'] == 'true'):

        print "Your request has been Deleted"


def check_gap():
    request_url = (BASE_url + 'receive/checkgap?xpub=%s&key=%s') % (my_xpub , my_api_key)
    print 'GET request url : %s' % (request_url)
    gap = requests.get(request_url).json()
    if len(gap['gap']):
        print 'You have %d gap' %(gap['gap'])




