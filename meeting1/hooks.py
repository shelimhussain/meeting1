# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "meeting1"
app_title = "Meeting1"
app_publisher = "frappe"
app_description = "meeting 1"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "shelim@usense.co"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/meeting1/css/meeting1.css"
# app_include_js = "/assets/meeting1/js/meeting1.js"

# include js, css files in header of web template
# web_include_css = "/assets/meeting1/css/meeting1.css"
# web_include_js = "/assets/meeting1/js/meeting1.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "meeting1.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "meeting1.install.before_install"
# after_install = "meeting1.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "meeting1.notifications.get_notification_config"

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

doc_events = {
	"User": {
		"after_insert": "meeting1.api.make_orientation_meeting"
	}
}

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
# 		"meeting1.tasks.all"
# 	],
# 	"daily": [
# 		"meeting1.tasks.daily"
# 	],
# 	"hourly": [
# 		"meeting1.tasks.hourly"
# 	],
# 	"weekly": [
# 		"meeting1.tasks.weekly"
# 	]
# 	"monthly": [
# 		"meeting1.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "meeting1.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "meeting1.event.get_events"
# }

