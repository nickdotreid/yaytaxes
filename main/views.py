from django.template import Context, loader
from django.http import HttpResponse

def index(request):
	t = loader.get_template('main/index.html')
	c = Context()
	return HttpResponse(t.render(c))
