from django.db import models


class WordQuerySet(models.query.QuerySet):
    def show_SYM1(self):
        return self.filter(SYM1=False)

#filter things on query level
class WordManager(models.Manager):
    def get_queryset(self):
        #return super(WordManager, self).filter(SYM1=True)
            return WordQuerySet(self.model, using=self._db) #using database

    def show_SYM1(self):
        return self.get_queryset().show_SYM1()

    # def all(self, **kwargs): #show only those with this filter
    #     return super(WordManager, self).filter()
        #return self.all
    # def show_SYM(self): #filter to show those available in SYM
    #     return super(WordManager, self).filter(SYM1=True)


# Create your models here.
class Word(models.Model):
    index = models.PositiveIntegerField
    masculinitive1 = models.CharField('Маскулінітив', max_length=50)
    feminitive1 = models.CharField('Фемінітив', max_length=50)
    SYM1 = models.BooleanField('Чи є це слово у словнику?', default=False) #11 ch.dict
    link1 = models.SlugField('Посилання на словник', allow_unicode=True, max_length=200)
    plural1 = models.CharField(max_length=50)
    rodovy1 = models.CharField(max_length=50)
    davalny1 = models.CharField(max_length=50)
    znahidny1 = models.CharField(max_length=50)
    orudny1 = models.CharField(max_length=50)
    miscevy1 = models.CharField(max_length=50)
    klychny1 = models.CharField(max_length=50)
    def_sym1 = models.CharField(max_length=5000)
    def_our1 = models.CharField(max_length=5000)
    usage1 = models.CharField(max_length=10000)

    #use either objects or items
    objects = WordManager()
    #items = WordManager()

    #unicode in py3
    def __str__(self):
        return self.feminitive1

    def get_absolute_url(self):
        return "/words/get/%i" % self.id


    def show_links(self):
        if self.SYM1 == True:
            return self.link1
        else:
            return self.index #change else statement later
