from django.urls import path, include
from .views import (
    FormView,
    UniversityFacultyView,
    UniversityFacultyALLView,
    ApplicantListView,
    TimeSlot_ListView,
    ApplicantInterviewedListView,
    ApplicantNonInterviewedListView,
    RedirectView,
    AdminView,
    ThankYou_View,
    UniversityListView,
)

app_name = "Form"

urlpatterns = [
    path("recruitment_form/", FormView.as_view(), name="Recruitment Form"),
    path("thank_you/", ThankYou_View.as_view(), name="Thank You"),

    
    # For Admins
    path(
        "faculty_university/<int:u_id>/",
        UniversityFacultyView.as_view(),
        name="Univ Fac",
    ),
    path(
        "faculty_university_all/",
        UniversityFacultyALLView.as_view(),
        name="Univ Fac All",
    ),
    path("applicants_list/", ApplicantListView.as_view(), name="Applicant List"),
    path("slots_list/", TimeSlot_ListView.as_view(), name="TimeSlot List"),
    path(
        "applicants_interviewed_list/",
        ApplicantInterviewedListView.as_view(),
        name="Applicant Interviewed List",
    ),
    path(
        "applicants_non_interviewed_list/",
        ApplicantNonInterviewedListView.as_view(),
        name="Applicant Not Interviewed List",
    ),
    path("", RedirectView.as_view()),
    path("univ_list/", UniversityListView.as_view(), name="University List"),
    path('high_b_oard/', AdminView.as_view(), name='Admin Panel'), 
]
