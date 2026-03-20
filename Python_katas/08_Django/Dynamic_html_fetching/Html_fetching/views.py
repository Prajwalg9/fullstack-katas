from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

posts = {
    'Python': [
        'Python is a dynamically typed language',
        'Python has large community support',
        'Python has many libraries'
    ],

    'Java': [
        'Java is mostly used in application development',
        'Java supports OOPs and data structures',
        'Java is very popular'
    ],

    'C': [
        'C is a procedural programming language',
        'C is very fast and memory efficient',
        'C is widely used in system programming'
    ],

    'Cpp': [
        'Cpp supports both procedural and object-oriented programming',
        'Cpp is used in game development and competitive programming',
        'Cpp provides high performance'
    ],

    'JavaScript': [
        'JavaScript is mainly used for web development',
        'JavaScript runs in the browser',
        'JavaScript is used for frontend and backend development'
    ],

    'PHP': [
        'PHP is a server-side scripting language',
        'PHP is widely used for web development',
        'PHP works well with databases like MySQL'
    ],

    'SQL': [
        'SQL is used to manage databases',
        'SQL is used to retrieve and manipulate data',
        'SQL works with relational databases'
    ],

    'HTML': [
        'HTML is used to structure web pages',
        'HTML defines the content of a webpage',
        'HTML is not a programming language'
    ],

    'CSS': [
        'CSS is used for styling web pages',
        'CSS controls layout, colors, and fonts',
        'CSS improves website appearance'
    ]
}


# Create your views here.
def home(request):
    posts_list = []
    for key, value in posts.items():
        posts_list.append(key)
    content="<h1>Post Links:</h1><ul>"
    for post in posts_list:
        paths = reverse('post', args=(post,))
        content += f'<li> <a href="{paths}">{post}</a></li>'
    content += "</ul>"
    return HttpResponse(content)


def post(request, post):
    if post not in posts:
        return HttpResponse("Post not found")

    points = posts[post]

    return render(
        request,
        'Html_fetching/home.html',
        {
            'topic': post,
            'point1': points[0],
            'point2': points[1],
            'point3': points[2],
        }
    )