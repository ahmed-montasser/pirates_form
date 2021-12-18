from django.urls import path, include
from .views import (
    FormView,
    UniversityFacultyView,
    UniversityFacultyALLView,
    ApplicantListView,
    TimeSlot_ListView,
    TimeSlot_CreateView,
    TimeSlot_DeleteView,
    TimeSlot_EditView,
    ApplicantAdmin_EditView,
    Faculty_EditView,
    Faculty_CreateView,
    University_CreateView,
    University_EditView,
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
    path("slots_create/", TimeSlot_CreateView.as_view(), name="TimeSlot Create"),
    path(
        "slots_delete/<int:pk>/", TimeSlot_DeleteView.as_view(), name="TimeSlot Delete"
    ),
    path("slots_edit/<int:pk>/", TimeSlot_EditView.as_view(), name="TimeSlot Update"),
    path(
        "applicants_edit/<int:pk>/",
        ApplicantAdmin_EditView.as_view(),
        name="Applicant Edit",
    ),
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
    path("faculties_edit/<int:pk>/", Faculty_EditView.as_view(), name="Faculty Update"),
    path("faculties_create/", Faculty_CreateView.as_view(), name="Faculty Create"),
    path(
        "univ_edit/<int:pk>/", University_EditView.as_view(), name="University Update"
    ),
    path("univ_create/", University_CreateView.as_view(), name="University Create"),
    path("high_b_oard/", AdminView.as_view(), name="Admin Panel"),
    path("", RedirectView.as_view()),
    path("univ_list/", UniversityListView.as_view(), name="University List"),
]
