import pandas as pd
import IPython
from geopy.geocoders import GoogleV3
from time import sleep
def getZips():
    d = pd.read_csv('guardian_with_zips.csv')
    d['full_address'] = d['streetaddress'] + ', ' + d['city'] + ' ' + d['state']
    #g = geocoder.google("453 Booth Street, Ottawa ON")
    geocoder = GoogleV3()
    #d['zipcode'] = None
    for i in range(len(d)):
        if str(d.iloc[i]['zipcode']) != 'nan':
            print 'Already have zipcode for', i,  str(d.iloc[i]['zipcode'])
            continue
        try:
            address = geocoder.geocode(d.iloc[i]['full_address'], timeout = 10).address
            print i, 'orig address', d.iloc[i]['full_address']
            print 'mapped to', address
            zipcode = address.split(',')[-2].split()[1]
            d['zipcode'].iloc[i] = zipcode
            print 'zipcode', zipcode
            sleep(1)
            d.to_csv('guardian_with_zips.csv')
        except:
            print 'Error with', d.iloc[i]['full_address']
        

    #IPython.embed()
getZips()