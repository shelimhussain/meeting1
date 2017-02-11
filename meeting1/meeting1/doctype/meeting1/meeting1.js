// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt


frappe.ui.form.on('Meeting1', {
	send_emails: function(frm) {
		if(frm.doc.status === "Planned"){
			frappe.call({
				method: "meeting1.api.send_invitation_emails",
				args: {
					meeting: frm.doc.name,
				},
				callback: function(r) {
				}
			});
		}
	},
	refresh: function(frm) {

	}
});


frappe.ui.form.on('Meeting Attended', {
	attendee: function(frm, cdt, cdn) {
		var attendee = frappe.model.get_doc(cdt, cdn);
		if(attendee.attendee){
			frappe.call({
				method: "meeting1.meeting1.doctype.meeting1.meeting1.get_full_name",
				args: {
					attendee: attendee.attendee
				},
				callback: function(r){
					frappe.model.set_value(cdt, cdn, "full_name", r.message);
				}
			});
		}else{
			frappe.model.set_value(cdt, cdn, "full_name", null);
		}
	}
});




