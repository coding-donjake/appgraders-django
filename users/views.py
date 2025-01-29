from django.http import JsonResponse
from django.shortcuts import render

from users.models import Account, User

# Create your views here.


def login(request):
    return JsonResponse(
        {
            "type": "test",
            "msg": "Log-in a test.",
        },
        status=200,
    )


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name", "")
        suffix = request.POST.get("suffix", "")
        gender = request.POST.get("gender")
        birth_date = request.POST.get("birth_date")

        if Account.objects.filter(username=username).exists():
            return JsonResponse(
                {
                    "type": "duplicate username",
                    "msg": "Username is already taken.",
                },
                status=409,
            )

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            suffix=suffix,
            gender=gender,
            birth_date=birth_date,
        )
        user.save()

        account = Account.objects.create(
            username=username,
            password=password,
            status=1,
            user=user,
        )
        account.set_password(password)
        account.save()

        return JsonResponse(
            {
                "type": "created account",
                "msg": "Account is created.",
            },
            status=201,
        )

    return JsonResponse(
        {
            "type": "invalid request type",
            "msg": "Invalid request.",
        },
        status=400,
    )
