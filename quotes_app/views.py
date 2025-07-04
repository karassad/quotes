import random

from django.shortcuts import render, get_object_or_404, redirect

from quotes_app.models import Quote


# Create your views here.
def random_quote(request):
    quotes = list(Quote.objects.all())
    if not quotes:
        return render(request, "quotes_app/no_quotes.html")

    weights = [q.weight for q in quotes]

    selected_quote = random.choices(quotes, weights=weights, k=1)[0]

    # Увеличиваем счетчик просмотров
    selected_quote.views += 1
    selected_quote.save()

    #собираем готовую html страницу
    return render(request, "quotes_app/random_quote.html", {"quote": selected_quote})

def like_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    quote.likes += 1
    quote.save()
    return redirect('/')

def dislike_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    quote.likes += 1
    quote.save()
    return redirect('/')