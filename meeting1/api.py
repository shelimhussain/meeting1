import frappe
from frappe import _
from frappe.utils import nowdate, add_days

@frappe.whitelist()
def send_invitation_emails(meeting):

	meeting = frappe.get_doc("Meeting1", meeting)
	meeting.check_permission("email")

	if meeting.status == "Planned":
		frappe.sendmail(
			recipients=[d.attendee for d in meeting.attendees],
			sender=frappe.session.user,
			subject=meeting.title,
			message=meeting.invitation_message,
			reference_doctype=meeting.doctype,
			reference_name=meeting.name
		) 

		meeting.status="Invitation Sent"
		meeting.save()
		
		frappe.msgprint(_("Invitation Sent"))
		
	else:
		frappe.msgprint(_("Meeting Status must be 'planned'"))
		
@frappe.whitelist()
def get_meetings(start, end):
	if not frappe.has_permission("Meeting1", "read"):
		raise frappe.PermissionError
		
	return frappe.db.sql("""select 
		timestamp(`date`,from_time) as start,
		timestamp(`date`,to_time) as end,
		name,
		title,
		status,
		0 as allDay
	from `tabMeeting1`
	where `date` between %(start)s and %(end)s""",{
		"start": start,
		"end": end
	},as_dict=True
	)
	
def make_orientation_meeting(doc,method):
	"""create a orientation meeting when a new user is added"""
	meeting = frappe.get_doc({
		"doctype": "Meeting1",
		"title": "Orientaion for {0}".format(doc.first_name),
		"date": add_days(nowdate(),1),
		"from_time": "09:00",
		"to_time": "09:30",
		"status": "Planned",
		"attendees": [{
			"attendee": doc.name
		}]
	})
	#The system manager might not have permission to create a meeting
	meeting.flags.ignore_permissions= True
	meeting.insert()
	
	frappe.msgprint(_("Orientation meeting created"))
	
