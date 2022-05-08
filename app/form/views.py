from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
from .models import University, Faculty, TimeSlot, FormApplierModel
from django.http import JsonResponse
from django.urls import reverse_lazy
from .forms import ApplicantsForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class FormView(View):
    def get(self, request):
        universities = University.objects.all()
        time_slots = TimeSlot.objects.all()
        ctx = {"universities": universities, "time_slots": time_slots}
        error_message = request.session.get("error_message", False)
        if error_message:
            ctx["error_message"] = error_message
            del (request.session["error_message"])
        return render(request=request, context=ctx, template_name="form/form.html")

    def post(self, request):
        applicant_first_name = request.POST.get("first_name", None)
        applicant_last_name = request.POST.get("last_name", None)
        applicant_email = request.POST.get("email", None)
        applicant_mobile_number = request.POST.get("mobile_number", None)
        applicant = FormApplierModel.objects.filter(
            email=applicant_email, mobile_number=applicant_mobile_number
        )
        if applicant.exists():

            request.session["error_message"] = "Credentials were applied before"
            return redirect(reverse_lazy("Pirates Form:Recruitment Form"))
        else:
            applicant_university_id = request.POST.get("university", None)

            applicant_faculty_id = request.POST.get("faculty", None)

            applicant_department = request.POST.get("department", False)

            applicant_first_preference = request.POST.get("first_preference", None)
            applicant_second_preference = request.POST.get("second_preference", None)
            applicant_time_slot_id = request.POST.get("time_slot", None)
            applicant_academic_year = request.POST.get("academic_year", None)

            t = get_object_or_404(TimeSlot, id=int(applicant_time_slot_id))
            f = FormApplierModel(
                first_name=applicant_first_name,
                last_name=applicant_last_name,
                email=applicant_email,
                mobile_number=applicant_mobile_number,
                first_preference=applicant_first_preference,
                second_preference=applicant_second_preference,
                time_slot=t,
                academic_year=applicant_academic_year,
            )

            if applicant_university_id == "other":
                applicant_university_other = request.POST.get("university_other", False)
                if applicant_university_other:
                    f.university_other = applicant_university_other
            else:
                f.university = University.objects.get(id=int(applicant_university_id))

            if applicant_faculty_id == "other":
                applicant_faculty_other = request.POST.get("faculty_other", False)
                if applicant_faculty_other:
                    f.faculty_other = applicant_faculty_other
            else:
                faculty_ = Faculty.objects.get(id=int(applicant_faculty_id))
                f.faculty = faculty_
                if faculty_.faculty.lower() == "engineering":
                    if applicant_department:
                        if applicant_department == "other":
                            f.department = applicant_department
                            applicant_department_other = request.POST.get(
                                "department_other", False
                            )
                            if applicant_department_other:
                                f.department_other = applicant_department_other
                        else:
                            f.department = applicant_department

            try:
                f.save()
                t.capacity -= 1
                t.save()

            except Exception as e:
                request.session["error_message"] = "Check information provided"
                return redirect(reverse_lazy("Pirates Form:Recruitment Form"))

            return redirect(reverse_lazy("Pirates Form:Thank You"))


class ThankYou_View(View):
    def get(self, request):
        return render(request=request, template_name="form/thank_U.html")


class UniversityFacultyView(View):
    def get(self, request, u_id):
        university = get_object_or_404(University, id=u_id)
        if university.faculties.exists():
            f = university.faculties.all().values()
            faculties = []
            for fac in f:
                faculties.append(fac)
            return JsonResponse(faculties, safe=False)
        else:
            return None


class UniversityFacultyALLView(View):
    def get(self, request):
        f = Faculty.objects.all().values()
        if f.count() > 0:
            faculties = []
            for fac in f:
                faculties.append(fac)
            return JsonResponse(faculties, safe=False)
        else:
            return None


class UniversityListView( LoginRequiredMixin,ListView):
    model = University
    template_name = "form/university_list.html"


class ApplicantListView(LoginRequiredMixin,ListView):
    model = FormApplierModel
    template_name = "form/formappliermodel_list.html"


class ApplicantNonInterviewedListView(LoginRequiredMixin,ListView):
    model = FormApplierModel
    template_name = "form/formappliermodel_non_interviewed_list.html"


class ApplicantInterviewedListView(LoginRequiredMixin,ListView):
    model = FormApplierModel
    template_name = "form/formappliermodel_interviewed_list.html"


class TimeSlot_ListView(LoginRequiredMixin,View):
    def get(self, request):
        timeslot_list = TimeSlot.objects.all()
        timeslot_applicants = []
        for timeslot in timeslot_list:
            applicants = FormApplierModel.objects.filter(time_slot=timeslot)
            timeslot_applicants.append({"timeslot": timeslot, "applicants": applicants})

        ctx = {"timeslot_applicants": timeslot_applicants}
        return render(
            request=request, template_name="form/timeslot_list.html", context=ctx
        )


class ApplicantAdmin_EditView(LoginRequiredMixin,View):
    def get(self, request, pk):
        f = get_object_or_404(FormApplierModel, id=pk)
        form = ApplicantsForm(instance=f)
        ctx = {"form": form}
        return render(
            request=request, context=ctx, template_name="form/applicants_admin.html"
        )

    def post(self, request, pk):
        f = get_object_or_404(FormApplierModel, id=pk)
        form = ApplicantsForm(request.POST, instance=f)

        if not form.is_valid():
            ctx = {"form": form}
            return render(
                request=request, context=ctx, template_name="form/applicants_admin.html"
            )
        form.save()
        return redirect(reverse_lazy("Pirates Form:Applicant List"))


class TimeSlot_CreateView(LoginRequiredMixin,CreateView):
    model = TimeSlot
    fields = "__all__"
    template_name = "form/slots_watch.html"
    success_url = reverse_lazy("Pirates Form:TimeSlot List")


class TimeSlot_EditView(LoginRequiredMixin,UpdateView):
    model = TimeSlot
    fields = "__all__"
    template_name = "form/slots_watch.html"
    success_url = reverse_lazy("Pirates Form:TimeSlot List")


class TimeSlot_DeleteView(LoginRequiredMixin,DeleteView):
    model = TimeSlot
    fields = "__all__"
    template_name = "form/timeslot_confirm_delete.html"
    success_url = reverse_lazy("Pirates Form:TimeSlot List")


class University_CreateView(CreateView):
    model = University
    fields = "__all__"
    template_name = "form/university_watch.html"
    success_url = reverse_lazy("Pirates Form:Applicant List")


class University_EditView(UpdateView):
    model = University
    fields = "__all__"
    template_name = "form/university_watch.html"
    success_url = reverse_lazy("Pirates Form:Applicant List")


class Faculty_CreateView(CreateView):
    model = Faculty
    fields = "__all__"
    template_name = "form/faculty_watch.html"
    success_url = reverse_lazy("Pirates Form:Applicant List")


class Faculty_EditView(UpdateView):
    model = Faculty
    fields = "__all__"
    template_name = "form/faculty_watch.html"
    success_url = reverse_lazy("Pirates Form:Applicant List")


class RedirectView(View):
    def get(self, request):
        return redirect(reverse_lazy("Pirates Form:Recruitment Form"))


class AdminView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request=request, template_name="form/admin_panel.html")
