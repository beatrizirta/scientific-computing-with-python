# Using Web Services
# XML

def basics():
	print('beatriz')
	#<person>
	#<name>Chuck</name>
	#<phone type="intl"
	#+1 734 303 4456
	#</phone>
	#<email hide="yes />"
	#</person>


# XML Schema -> User to specify a contract between systems
# XML Document or XML Schema Contract -> Validator

def XSD_Structure():
	print('beatriz')
	#<person>
	#<lastname>Severance</lastname>
	#<age>17<age>
	#<dateborn>2001-04-17</dateborn>
	#</person>

	#<xs:complexType name="person">
	#<xs:sequence>
	#<xs:element name="lastname" type="xs.string"/>
	#<xs.element name+"age"type 


	
	#data = '''<person>
		#<name>Beatriz</name>
		#<phone type="intl">
			#+1 734 303 4456
		#</phone>
		#<email hide="yes/">
	#</person>'''

#tree = ET.fromstring(data)
#print('Name:', tree.find('name').text)
#print('Attr:', tree.find('email').get('hide'))


def xml_funcionou():
	import xml.etree.ElementTree as ET
	input = '''<stuff>
		<users>
			<user x="2">
				<id>001</id>
				<name>Chuck</name>
			</user>
			<user x="7">
				<id>009</id>
				<name>Brent</name>
			</user>
		</users>
	</stuff>'''

	stuff = ET.fromstring(input)
	lst = stuff.findall('users/user')
	print('User count:', len(lst))
	for item in lst:
		print('Name', item.find('name').text)
		print('Id', item.find('id').text)
		print('Attribute', item.get("x"))


#xml_funcionou()


#_______________________________
#JavaScript Object Notation
#JSON -> Object literal notation in JavaScript
#JSON represents data as nested "lists" and "dictionaries"
def jsontests():

	import json
	data = '''{
		"name" : "Beatriz",
		"phone" : {
		    "type" : "intl",
		    "number" : "+1 734 303 4456"
		},
		"email" : {
			"hide" : "yes"
		}
	}'''

	info = json.loads(data)
	print('Name:',info["name"])
	print('Hide:',info["email"]["hide"])


jsontests()

def jason_naofuncionou():
	import json
	inpput = '''{
		{"id" : "001",
		 "x" : "2",
		 "name" : "Chuck"
		 } ,
		 {"id" : "009",
		 "x" : "7",
		 "name" : "Beatriz"
		 }
	}'''

	info = json.loads(input)
	print('User count:', len(info))
	for item in info:
		print('Name', item['name'])
		print('Id', item['id'])
		print('Attribute', item['x'])

jason_naofuncionou()