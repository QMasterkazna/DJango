from django.shortcuts import render


def main(requests):
    return render(requests, 'main/main.html')

