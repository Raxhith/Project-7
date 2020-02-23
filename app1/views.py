from django.shortcuts import render
import datetime

def dis_data(request):
	data = datetime.datetime.now()
	print(data)
	my_dict = {'ins_time':data}
	return render(request=request, template_name='App1/display.html',context=my_dict)
