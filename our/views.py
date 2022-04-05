#i have created project sonu vishwakarma
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  return render(request ,'index.html')


# def index(request):
#
#     return HttpResponse("<h1>sonu vishwakarma </h1> <a href='/'>back</a>")
                    #to give the link of any website
    #to give the link we use ''' dsfdsf'''
                       # <a href="https://www.google.com/search?q=sonu+vishwakarma&oq=sonu&aqs=chrome.1.69i57j69i59l3j69i61l2.2969j0j15&sourceid=chrome&ie=UTF-8">VISHWKARMA</a>''')
def about(request):
    return HttpResponse(" about hello sonu vishwkarma"
                        "<div> sonu</div> <div> vishwakarma</div>"
                        "<strong>sonu</storng>"

                        )

def home(request):
    return HttpResponse("this site is home<a href='/'>back</a>")

def contact(request):
    #get the text
    global params
    djtext = request.POST.get('text','default')
    Num = request.POST.get('name','default')
    fullcap = request.POST.get('uppercase','off')
    Error = request.POST.get('error','default')
    lenght = request.POST.get('lenghts','default')
    extraspace = request.POST.get('space','default')
    newlines = request.POST.get('newline','default')
    removepunc = request.POST.get('removepunc','off')# you can use off and default
    print(removepunc)
    analyzed = djtext
    num = Num
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,c<>./?@#$%^&*_~'''

        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'MIND CODER', 'analyzed_text': analyzed}
        djtext =analyzed
        # analyzis the text
        # return HttpResponse("this is contact site<a href='/'>back</a>")
        # return render(request, 'analysis.html', params)
    if (fullcap == "on"):
        analyzed = ""
        for car in djtext:
            analyzed = analyzed + car.upper()
        params = {'purpose': 'uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analysis.html', params)
    if (newlines == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "/r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'removed new lines', 'analyzed_text': analyzed}
        djtext= analyzed
        # return render(request, 'analysis.html', params)
    if (extraspace == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'space remove', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analysis.html', params)
    if (lenght == "on"):

        leng = (len(analyzed))

        params = {'purpose': 'lenght of your text sir', 'analyzed_text': analyzed,'lenght':leng}
        djtext=analyzed
        # return render(request, 'analysis.html', params)
        # return  HttpResponse(leng)

    if (removepunc != "on" and fullcap != "on" and newlines != "on" and extraspace != "on" and lenght!="on"):
        return HttpResponse("please the any operation  and try again sir")
    return render(request, 'analysis.html', params)

    # else:
    #     enter = Error
    #     return HttpResponse(enter)


def link(request):
    return HttpResponse("this is link <a href='/'>back</a>")