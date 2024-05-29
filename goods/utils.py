from goods.models import Products
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


def q_search(querry):
    if querry.isdigit() and len(querry) <= 5:
        return Products.objects.filter(id=int(querry))

    vector = SearchVector("name", "description")
    query = SearchQuery(querry)

    return Products.objects.annotate(rank=SearchRank(vector, query)).order_by("rank")

    # keywords = [word for word in querry.split() if len(word) > 2]

    # q_objects = Q()

    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)

    # return Products.objects.filter(q_objects)
