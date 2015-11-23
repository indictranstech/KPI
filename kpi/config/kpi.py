from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		
		{
			"label": _("Masters"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Ferro Pipeline",
					"description": _("Ferro Pipeline Master"),
				},
				{
					"type": "doctype",
					"name": "Ferro OrderFU",
					"description": _("Ferro OrderFU Master"),
				}
				
			]
		}
	]
