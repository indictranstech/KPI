# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "kpi"
app_title = "KPI"
app_publisher = "New Indictrans Technologies Pvt Ltd."
app_description = "KPI"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@indictranstech.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/kpi/css/kpi.css"
# app_include_js = "/assets/kpi/js/kpi.js"

# include js, css files in header of web template
# web_include_css = "/assets/kpi/css/kpi.css"
# web_include_js = "/assets/kpi/js/kpi.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "kpi.install.before_install"
# after_install = "kpi.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "kpi.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"kpi.tasks.all"
# 	],
# 	"daily": [
# 		"kpi.tasks.daily"
# 	],
# 	"hourly": [
# 		"kpi.tasks.hourly"
# 	],
# 	"weekly": [
# 		"kpi.tasks.weekly"
# 	]
# 	"monthly": [
# 		"kpi.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "kpi.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "kpi.event.get_events"
# }
doc_events = {
	"DocType":{
		"on_update": "kpi.kpi.zoho_xml_parser.configure_kpi",
	}
}
