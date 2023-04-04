from . import __version__ as app_version

app_name = "server_manager"
app_title = "Server Manager"
app_publisher = "RamjanAli Lal"
app_description = "Server Manager System"
app_email = "ramjanali@erevivetechnologies.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/server_manager/css/server_manager.css"
# app_include_js = "/assets/server_manager/js/server_manager.js"

# include js, css files in header of web template
# web_include_css = "/assets/server_manager/css/server_manager.css"
# web_include_js = "/assets/server_manager/js/server_manager.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "server_manager/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "server_manager.utils.jinja_methods",
#	"filters": "server_manager.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "server_manager.install.before_install"
# after_install = "server_manager.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "server_manager.uninstall.before_uninstall"
# after_uninstall = "server_manager.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "server_manager.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"server_manager.tasks.all"
#	],
#	"daily": [
#		"server_manager.tasks.daily"
#	],
#	"hourly": [
#		"server_manager.tasks.hourly"
#	],
#	"weekly": [
#		"server_manager.tasks.weekly"
#	],
#	"monthly": [
#		"server_manager.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "server_manager.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "server_manager.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "server_manager.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["server_manager.utils.before_request"]
# after_request = ["server_manager.utils.after_request"]

# Job Events
# ----------
# before_job = ["server_manager.utils.before_job"]
# after_job = ["server_manager.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"server_manager.auth.validate"
# ]
