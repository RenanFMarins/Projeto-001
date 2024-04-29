from django.shortcuts import get_list_or_404, get_object_or_404, render

from coworking.models import Coworking


def home(request):
    coworkings = Coworking.objects.filter(
        is_published=True,
    ).order_by('id')

    return render(request, 'coworking/pages/home.html', context={
        'coworkings': coworkings})


def category(request, category_id):
    coworkings = get_list_or_404(
        Coworking.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )

    return render(request, 'coworking/pages/category.html', context={
        'coworkings': coworkings,
        'title': f'{coworkings[0].category.name} - Category | '
    })


def coworking(request, id):
    coworking = get_object_or_404(Coworking, pk=id, is_published=True,)
    return render(request, 'coworking/pages/coworking-view.html', context={
        'coworking': coworking,
        'is_detail_page': True,
    })
