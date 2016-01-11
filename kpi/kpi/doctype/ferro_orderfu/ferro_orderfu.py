# -*- coding: utf-8 -*-
# Copyright (c) 2015, New Indictrans Technologies Pvt Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import date_diff

class FerroOrderFU(Document):
	pass
@frappe.whitelist()
def get_week(date):
	import datetime
	tdate = datetime.datetime.strptime(date, '%Y-%m-%d') 
	return	tdate.isocalendar()[1]

@frappe.whitelist()
def get_datediff(date,date1):
	d = date_diff(date, date1)
	frappe.errprint(d)
	return d