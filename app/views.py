from django.shortcuts import render

# Create your views here.
def condition(request):
  d={'a':100,'b':254,'c':423}
  return render(request,'condition.html',context=d)
