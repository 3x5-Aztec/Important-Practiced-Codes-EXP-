import requests
import json
import xmltodict

url="https://epm10.hostanalytics.com/HostApi/HostAPI_StateFree.asmx"
headers = {'Content-Type': 'text/xml','SOAPAction': 'http://www.HostAnalytics.com/API/SOAP/StateFree/Common/2009/03/19/GLData_RetrieveWithLogin'}
body = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GLData_RetrieveWithLogin xmlns="http://www.HostAnalytics.com/API/SOAP/StateFree/Common/2009/03/19">
      <LoginName></LoginName>
      <Password></Password>
      <TenantCode></TenantCode>
      <FilterCollection>
        <GLDataFilter>
          <Field>FiscalYear</Field>
          <FieldOperator>Equals</FieldOperator>
          <Value>
            <string>2020</string>
            </Value>
        </GLDataFilter>
        
        <GLDataFilter>
          <Field>Scenario</Field>
          <FieldOperator>Equals</FieldOperator>
          <Value>
            <string>2020 Budget</string>
            </Value>
        </GLDataFilter>
        
        <GLDataFilter>
          <Field>AmountType</Field>
          <FieldOperator>Equals</FieldOperator>
          <Value>
            <string>MTD</string>
            </Value>
        </GLDataFilter>
        
      </FilterCollection>
    </GLData_RetrieveWithLogin>
  </soap:Body>
</soap:Envelope>"""

response = requests.post(url,data=body,headers=headers)
# print (response.content)

# C:\Users\Diacto1\EXP\XML Request Handling
with open(r'C:\Users\Diacto1\EXP\XML Request Handling\Planful.xml', 'wb') as file:
    file.write(response.content)

with open(r"C:\Users\Diacto1\EXP\XML Request Handling\Planful.xml") as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        xml_file.close()
        json_data = json.dumps(data_dict, indent=10)
        
        with open(r'C:\Users\Diacto1\EXP\XML Request Handling\data.json', "w") as json_file:
            json_file.write(json_data)