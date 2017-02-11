frappe.views.calendar["Meeting1"] = {
	field_map: {
		"start": "start",
		"end": "end",
		"id": "name",
		"title": "title",
		"status": "status",
		"allDay": "allDay",
	},
	get_events_method: "meeting1.api.get_meetings"
}