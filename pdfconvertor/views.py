# Create your views here.

from django.http import HttpResponse


from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson

from django.shortcuts import render
# module to convert html/css to pdf
from weasyprint import HTML, CSS


@login_required
@csrf_exempt
def writepdf(request):
    if request.method == 'POST':
        json_data = simplejson.loads(request.body)
        try:
            data = json_data['css']
            if (data == 'Professional'):
                with open('api/resume-pre-templates/bootstrap-file', 'r') as content:
                    cssData = content.read()
                
                with open('api/resume-pre-templates/design-professional', 'r') as content:
                    cssData += content.read()
                print cssData
                #response = HttpResponse(mimetype='application/pdf')
                
                HTML(string=json_data['html']).write_pdf('pdf/'+str(request.user)+'-'+json_data['no'] +'.pdf',stylesheets=[CSS(string=cssData)])
                #return render(response,'/',{})
        except KeyError:
          HttpResponseServerError("Malformed data!")
        
        return HttpResponse(request.body,mimetype='application/json')
        
    else:
        print 'data'
        return render(request, 'landing_page/index.html', {})