# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

def onValueChange(par, prev):
	return

def onPulse(par):
	if par.name == 'Updateall':
		parent().Set_all_lights()	
	
	elif par.name == 'Updatebysettings':
		parent().Update_all_by_settings()
	
	elif par.name == 'Setupindividuallights':
		parent().Clear_and_setup_lights()
			
	else:
		parent().Update_light_by_par_index(tdu.digits(par.name))

	return

def onExpressionChange(par, val, prev):
	return

def onExportChange(par, val, prev):
	return

def onEnableChange(par, val, prev):
	return

def onModeChange(par, val, prev):
	return
	