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
				},
				{
					"type": "doctype",
					"name": "Ferro Hub",
					"description": _("Ferro Hub Master"),
				},
				{
					"type": "doctype",
					"name": "Ferro Item",
					"description": _("Ferro Item Master"),
				},
				{
					"type": "doctype",
					"name": "MAS_PO_Master",
					"description": _("MAS PO Master"),
				},
				{
					"type": "doctype",
					"name": "MAS_WO_Master",
					"description": _("MAS WO Master"),
				},
			]
		},
		{
			"label": _("MB Doctype"),
			"items": [
				{
					"type": "doctype",
					"name": "mb_monthly_costing",
					"description": _("mb_monthly_costing Setup"),
				},
				{
					"type": "doctype",
					"name": "mb_monthly_industry_trends",
					"description": _("mb_monthly_industry_trends Setup"),
				},
				{
					"type": "doctype",
					"name": "mb_monthly_inventory",
					"description": _("mb_monthly_inventory Setup"),
				},
				{
					"type": "doctype",
					"name": "MB Territory",
					"description": _("MB Territory Setup"),
				},
				{
					"type": "doctype",
					"name": "mb_weekly_inventory",
					"description": _("MB Weekly_Inventory Setup"),
				},
				{
					"type": "doctype",
					"name": "mb_weekly_receivable_data",
					"description": _("mb_weekly_receivable_data Setup"),
				},
				{
					"type": "doctype",
					"name": "mb_weekly_sales_data",
					"description": _("mb_weekly_sales_data Setup"),
				},
				{
					"type": "doctype",
					"name": "mb_weekly_servicing_data",
					"description": _("mb_weekly_servicing_data Setup"),
				},
			]
		},
		{
			"label": _("Report"),
			"items": [
				{
					"type": "doctype",
					"name": "Owner",
					"description": _("Owner Report"),
				},
				{
					"type": "doctype",
					"name": "Sales Report",
					"description": _("sales Report"),
				},
				{
					"type": "doctype",
					"name": "Sales Reporting",
					"description": _("sales Reporting"),
				},
				{
					"type": "doctype",
					"name": "Sales Target",
					"description": _("sales target"),
				},
				{
					"type": "doctype",
					"name": "test",
					"description": _("test"),
				},
				{
					"type": "doctype",
					"name": "year",
					"description": _("year"),
				},
				{
					"type": "doctype",
					"name": "ZOHO Config",
					"description": _("ZOHO Config"),
				},

			]
		}
	]
