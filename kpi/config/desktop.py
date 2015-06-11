# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"KPI": {
			"color": "#589494",
			"icon": "octicon octicon-file-binary",
			"type": "module",
			"label": _("Easy Feed")
		},
		"My Reports": {
			"color": "#e67e22",
			"icon": "octicon octicon-pulse",
			"type": "module",
			"label": _("Easy Reports")
		}
	}
