from haystack import indexes
from myaccount.models import bizProject

class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    created_at = indexes.DateTimeField(model_attr='created_at')
    updated_at = indexes.DateTimeField(model_attr='updated_at')

    def get_model(self):
        return bizProject

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()