frappe.provide('erpnext');

// add toolbar icon
$(document).bind('toolbar_setup', function() {
	frappe.app.name = "Increasy";

	$('.navbar-home').html('Increasy');
});