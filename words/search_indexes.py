 # import datetime
 from haystack import indexes
 from words.models import Word

 class WordIndex(indexes.SearchIndex, indexes.Indexable):
     masculinitive1 = indexes.CharField(document=True, use_template=True)
     feminitive1 = indexes.CharField(document=True, use_template=True)

     #content for autocomplete
     content_auto = indexes.EdgeNgramField(model_attr='masculinitive1')

     def get_model(self):
         return Word

    def index_queryset(self, using=None):
        # used when the entire index for model is updated
        return self.get_model().objects.all
