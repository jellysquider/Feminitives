from django.shortcuts import render
from django.http import HttpResponse
from words.models import Word
from words.forms import WordForm
from django.template.context_processors import csrf
from haystack.query import SearchQuerySet
from django.template import Context #pass context to the html and render itself
from django.template.loader import get_template
from dict.forms import ContactForm


# Create your views here.
def words(request):
    language = 'ukr' #stored in COOKIES
    session_language = 'ukr' #stored inside the session

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    args = {} #dict type
    args.update(csrf(request))

    args['words'] = Word.objects.all()
    args['language'] = language
    args['session_language'] = session_language

    return render(request, 'words.html', args)
                #  {'words': words,
                #  'language' : language,
                #  'session_language' : session_language})

def word(request, word_id=1):
    word = Word.objects.get(id=word_id)
    return render(request, 'word.html',
                 {'word': word })

def word_template(request):
    word = "філософ"
    return render(request, 'word.html',
                    {'test': word })

def language(request, language='ukr'):
    response = HttpResponse("setting language to %s" % language)

    response.set_cookie('lang', language)

    request.session['lang'] = language

    return response

def create(request):
    if request.POST:
        form = WordForm(request.POST) #, request.FILES)
        if form.is_valid():
            form.save()
            # ix = open_dir(settings.WHOOSH_INDEX)
            # author = ix.author()
            # author.add_document(masculinitive1=a.masculinitive1, feminitive1=a.feminitive1,
            #                                         url=unicode(a.get_absolute_ulr()))
            # author.commit()
            return HttpResponse('/words/all')
    else:
        form = WordForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render(request, 'create_word.html', args)



def search_words(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    words = Word.objects.filter(masculinitive1__contains=search_text)

    return render(request, 'ajax_search.html', {'words' : words})



def index(request):
    # title = "Welcome"
    # if request.user.is_authenticated():
    #     title = "Hello %s" %(request.user)

    #add a form
    form = ContactForm(request.POST or None)
    context = {
        "form": form,
        }


    if form.is_valid():
        instance = form.save(commit=False)

        email = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get('full_name')
        if not full_name:
            full_name = "Анонім_ка"
        instance.full_name = full_name
        instance.save()
        # print (instance.email)
        # print (instance.timestamp)


    return render(request, 'index.html', context)



def qa(request):
        return render(request, 'q-a.html', {})
