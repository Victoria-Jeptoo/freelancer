from django.http import Http404
from django.shortcuts import render

SITE_NAME = "My Portfolio"
TAGLINE = "Graphic Artist - Web Designer - Illustrator"

ITEMS = [
    {"id": 1, "title": "Log Cabin", "image": "images/cabin.png",
     "description": "A cozy log cabin illustration."},
    {"id": 2, "title": "Tasty Cake", "image": "images/cake.png",
     "description": "A delicious cake illustration."},
    {"id": 3, "title": "Circus Tent", "image": "images/circus.png",
     "description": "A colourful circus tent."},
    {"id": 4, "title": "Controller", "image": "images/game.png",
     "description": "A game controller design."},
    {"id": 5, "title": "Locked Safe", "image": "images/safe.png",
     "description": "A locked safe illustration."},
    {"id": 6, "title": "Submarine", "image": "images/submarine.png",
     "description": "A yellow submarine illustration."},
]


def index(request):
    data = {
        "site_name": SITE_NAME,
        "tagline": TAGLINE,
        "items": ITEMS,
    }
    return render(request, "home.html", data)


def portfolio_detail(request, item_id):
    selected = None
    for item in ITEMS:
        if item["id"] == item_id:
            selected = item
    if selected is None:
        raise Http404("Portfolio item not found")
    return render(request, "portfolio_detail.html", {"item": selected, "site_name": SITE_NAME})


def about(request):
    return render(request, "about.html", {"site_name": SITE_NAME})


def contact(request):
    sent = False
    name = ""
    if request.method == "POST":
        name = request.POST.get("name")
        sent = True
    data = {
        "site_name": SITE_NAME,
        "sent": sent,
        "name": name,
    }
    return render(request, "contact.html", data)