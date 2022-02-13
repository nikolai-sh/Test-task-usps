import os
import csv
import requests
import threading
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

try:
    USERID = os.environ["USPS_USERID"]
except KeyError:
    raise SystemExit("Check the USPS_USERID!")
    
url = "https://secure.shippingapis.com/ShippingAPI.dll?API=Verify&"
input_filename = 'Python Quiz Input - Sheet1.csv'


def is_valid_adress(street, city, state, zipcode):
    xml = f'XML=<AddressValidateRequest USERID="{USERID}"><Address><Address1></Address1>\
                <Address2>{street}</Address2><City>{city}</City><State>{state}</State>\
                <Zip5>{zipcode}</Zip5><Zip4></Zip4></Address></AddressValidateRequest>'
    try:
        r = requests.get(url + xml)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
        
    return "Invalid" if "Address Not Found" in r.text else "Valid"


def write_to_csv(writer, company, street, city, state, zipcode):
    valid_res = is_valid_adress(street, city, state, zipcode)
    writer.writerow({
                    'Company': company, 'Street': street, 'City': city,
                    'St': state, 'ZIPCode': zipcode, 'AdressValidation': valid_res
                    })
    
    
def main():
    #read csv file
    with open(input_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        #write to new file with checking adress
        with open('AdressValidation.csv', 'w', newline='') as file:
            fieldnames = ['Company', 'Street', 'City', 'St', 'ZIPCode', 'AdressValidation']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            threads = []
            
            for row in reader:
                t = threading.Thread(target=write_to_csv, args=(writer, row['Company'], row['Street'],
                                                                row['City'], row['St'], row['ZIPCode']))
                t.start()
                threads.append(t)                             
            for t in threads:
                t.join()

                
if __name__ == "__main__":
    main()
    print("Process finished!")
   

