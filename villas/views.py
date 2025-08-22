from django.shortcuts import render, get_object_or_404
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Enquiry, Villa
from django.contrib import messages 

def home(request):
    return render(request, "main/home_combined.html")

def location(request):
    return render(request, 'main/location.html')

def overview(request):
    return render(request, 'main/overview.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def amenities(request):
    return render(request, 'main/amenities.html')

def payment_plan(request):
    return render(request, 'main/payment_plan.html')

def lead_submit(request):
    if request.method == "POST":
        # TODO: save lead / send email
        messages.success(request, "Thanks! We’ll send the brochure shortly.")
    return redirect("villas:payment_plan")

def callback_submit(request):
    if request.method == "POST":
        # TODO: save request / send email
        messages.success(request, "Thanks! We’ll call you back soon.")
    return redirect("villas:payment_plan")

def contact(request):
    return render(request, 'main/contact.html')

# gallery_images contains static-relative paths

def _get_client_ip(request):
    xff = request.META.get("HTTP_X_FORWARDED_FOR")
    return xff.split(",")[0].strip() if xff else request.META.get("REMOTE_ADDR")

@csrf_exempt
def web3forms_webhook(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid method")

    if request.content_type and "application/json" in request.content_type:
        try:
            data = json.loads(request.body.decode("utf-8"))
        except Exception:
            data = {}
    else:
        data = request.POST.dict()

    enquiry = Enquiry(
        name=data.get("name") or data.get("fullname") or "",
        email=data.get("email", ""),
        phone=data.get("phone") or data.get("tel", ""),
        message=data.get("message") or data.get("text") or "",
        property_type=data.get("property_type", ""),
        bedroom_type=data.get("bedroom_type", ""),
        requirements=data.get("requirements", ""),
        page_url=data.get("page_url", ""),
        referrer=data.get("referrer", ""),
        ip_address=_get_client_ip(request),
        user_agent=request.META.get("HTTP_USER_AGENT", ""),
    )
    enquiry.save()

    return JsonResponse({"ok": True, "saved_id": enquiry.id})