cur_frm.cscript.refresh = function(doc, dt, dn) {
	if (doc.link){
		show_report(doc.link)
	}
}
cur_frm.cscript.validate = function(doc,dt,dn){
	if (doc.link){
		show_report(doc.link)
	}
}
cur_frm.cscript.onload = function(doc,dt,dn){
	wrapper = $(cur_frm.get_field("display").wrapper)
	wrapper.empty()
	if (doc.link){
		show_report(doc.link)
	}
}
function show_report(link){
	wrapper = $(cur_frm.get_field("display").wrapper)
	wrapper.empty()
	wrapper.append(link)
}

