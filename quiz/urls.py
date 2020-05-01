try:
    from django.conf.urls import url
    from django.conf.urls.static import static
    from django.conf import settings
except ImportError:
    from django.urls import re_path as url

from .views import QuizListView, CategoriesListView, \
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList, \
    QuizMarkingDetail, QuizDetailView, QuizTake, QuizList, \
    QuestionList, CategoryList, ProgressList, MarkingList, UserRegistrationFormView, \
    UserLoginFormView, UserLogoutView, ContinueQuizTake


urlpatterns = [    

    url(r'^register/$', 
        view=UserRegistrationFormView.as_view(), 
        name='register'),

    url(r'^login/$', 
        view=UserLoginFormView.as_view(), 
        name='login'),

    url(r'^logout/$', 
        view=UserLogoutView.as_view(), 
        name='logout'),

    url(r'^list/$',
        view=QuizList.as_view(),
        name='quiz_list_index'),

    url(r'^$',
        view=QuizListView.as_view(),
        name='quiz_index'),

    url(r'^(?P<quiz_name>[\w-]+)/list/$',
        view=QuestionList.as_view(),
        name='question_list'),

    url(r'^category/$',
        view=CategoriesListView.as_view(),
        name='quiz_category_list_all'),

    url(r'^category/(?P<category_name>[\w|\W-]+)/list/$',
        view=CategoryList.as_view(),
        name='category_list'),
    
    url(r'^category/(?P<category_name>[\w|\W-]+)/$',
        view=ViewQuizListByCategory.as_view(),
        name='quiz_category_list_matching'),

    url(r'^progress/list$',
        view=ProgressList.as_view(),
        name='quiz_progress'),

    url(r'^progress/$',
        view=QuizUserProgressView.as_view(),
        name='quiz_progress'),

    url(r'^marking/list$',
        view=MarkingList.as_view(),
        name='quiz_marking'),

    url(r'^marking/$',
        view=QuizMarkingList.as_view(),
        name='quiz_marking'),

    url(r'^marking/(?P<pk>[\d.]+)/$',
        view=QuizMarkingDetail.as_view(),
        name='quiz_marking_detail'),

    #  passes variable 'quiz_name' to quiz_take view
    url(r'^(?P<slug>[\w-]+)/$',
        view=QuizDetailView.as_view(),
        name='quiz_start_page'),

    url(r'^(?P<quiz_name>[\w-]+)/take/$',
        view=QuizTake.as_view(),
        name='quiz_question'),

    url(r'^(?P<quiz_name>[\w-]+)/take/(?P<pk>[\d.]+)/$',
        view=ContinueQuizTake.as_view(),
        name='continue_quiz_question'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)