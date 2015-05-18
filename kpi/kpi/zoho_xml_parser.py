from __future__ import unicode_literals
import frappe
import frappe.defaults

from frappe.utils import cstr, cint, flt, comma_or, nowdate

from frappe import _ ,msgprint

"""
	Configure XML file for ZOHO Integration
"""
def configure_kpi(doc,method):
	"""
		remaining check con for single and child table
		what if there is no table in zoho
	"""
	if doc.module == 'Test Zoho' and doc.istable == 0 and doc.issingle == 0: 
		zoho_config_path = frappe.db.get_value("ZOHO Config","ZOHO Config","zoho_path")
		zoho_database = frappe.db.get_value("ZOHO Config","ZOHO Config","zoho_db_name")
		if zoho_config_path and zoho_database:
			"""
				1.Read XML File
				2.Check Whether table exists in XML DB Config file.
					-if yes update query
					-if no add new sub element and add attributes and query
				3.Write data to XML File
			"""
			update_xml_content(zoho_config_path,zoho_database,doc)

		else:
			frappe.msgprint("ZOHO Configuration Not Done Contact Administrator")

def update_xml_content(zoho_config_path,zoho_database,doc):
	from lxml import etree
	file_path = "{0}database_sql_queries.xml".format(zoho_config_path)
	xml_content = etree.parse(file_path)
	xml_root = xml_content.getroot()
	add_element = False
	
	for elem in xml_root.findall('Query'):
		if elem.get('tablename') == doc.name:
			query = build_query(doc)
			elem.text = elem.text.replace(elem.text,query)
			add_element = True

	if not add_element:
		sub_element = etree.SubElement(xml_root,'Query')
		sub_element.attrib["dbname"] = zoho_database
		sub_element.attrib["tablename"] = doc.name
		sub_element.attrib["importtype"] = "TRUNCATEADD"
		sub_element.attrib["matchingcols"] = ""
		sub_element.attrib["selectcols"] = ""
		sub_element.attrib["skiptop"] = ""
		query = build_query(doc)
		sub_element.text = query

	xml_content.write(file_path)		 			

def build_query(doc):
	field_list=[]
	for field in doc.get('fields'):
		field_list.append(field.fieldname)
	cols = (',').join(field_list)
	query="select {0} from `tab{1}`".format(cols,doc.name)
	return query
