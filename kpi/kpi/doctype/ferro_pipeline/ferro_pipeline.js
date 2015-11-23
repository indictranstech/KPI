frappe.ui.form.on("Ferro Pipeline", {
	onload: function(frm) {
	},
	refresh: function(frm) {
	var me = this
	if(!frm.doc.__islocal) {
			cur_frm.add_custom_button(__('Make Ferro Order'), function() {
				cur_frm.cscript.make_ferro_order(); });
		}
	}

});

cur_frm.cscript.make_ferro_order =function(){
	frappe.model.open_mapped_doc({
		method: "kpi.kpi.doctype.ferro_pipeline.ferro_pipeline.make_ferro_order",
		frm: cur_frm
	});

}
