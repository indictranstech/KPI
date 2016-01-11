frappe.ui.form.on("Ferro Pipeline", {
	// onload: function(frm) {
	// },
	refresh: function(frm) {
		var me = this
		if(!frm.doc.__islocal) {
			cur_frm.add_custom_button(__('Make Ferro Order'), function() {
				cur_frm.cscript.make_ferro_order(); 
			});
		}
	}

});

cur_frm.cscript.make_ferro_order =function(){
	frappe.model.open_mapped_doc({
		method: "kpi.kpi.doctype.ferro_pipeline.ferro_pipeline.make_ferro_order",
		frm: cur_frm
	});
}
<<<<<<< HEAD
cur_frm.add_fetch("Customer", "vendor_code", "vendor_code");
=======

//cur_frm.add_fetch("Customer", "vendor_code", "vendor_code");
>>>>>>> 82e4f96... Changes Of Final Requirement


// def check_lead_date(self):
// 		mod_db = frappe.db.get_value("Ferro Pipeline", self.lead_date, "")

// Date.prototype.getWeek = function() {
//   var onejan = new Date(this.getFullYea r(),0,1);
//   return Math.ceil((((this - onejan) / 86400000) + onejan.getDay()+1)/7);
// }

// var today = new Date();
// var weekNumber = today.getWeek();
// console.log(weekNumber); // Returns the week number as an integer