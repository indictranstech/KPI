# -*- coding: utf-8 -*-
# Copyright (c) 2015, New Indictrans Technologies Pvt Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
class FerroPipeline(Document):
	pass



@frappe.whitelist()
def make_ferro_order(source_name):
	target = get_mapped_doc("Ferro Pipeline", source_name, {
		"Ferro Pipeline": {
			"doctype": "Ferro OrderFU"
		}
	})
	return target

@frappe.whitelist()
def get_address(customer):
	return frappe.db.sql("""select city,state,email_id,phone from `tabAddress` where customer=%s""",(customer))

@frappe.whitelist()
def get_week_of_year(date):
	import datetime
	tdate = datetime.datetime.strptime(date, '%Y-%m-%d') 
	return	tdate.isocalendar()[1]
	#datetime.date.today().isocalendar()[1]
# @frappe.whitelist()
# def get_address(customer):
# 	return frappe.db.sql("""select city,state from `tabContact` where customer=%s""",(customer))	
	
