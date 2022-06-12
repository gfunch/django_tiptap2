from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from .models import Comment


@login_required
def tiptap_comments(request, *args, **kwargs):
    parent_model = kwargs["parent_model"]
    parent_model_id = kwargs["parent_model_id"]
    author = request.user.id
    text = kwargs["text"]
    node = kwargs["node"]
    loc_from = kwargs["loc_from"]
    loc_to = kwargs["loc_to"]
    if request.is_ajax:
        method = request.method
        if method == "POST":  # create a new comment
            parent_instance = parent_model.objects.get(id=parent_model_id)
            cmnt = Comment(
                content_object=parent_instance,
                author=request.user.id,
                text=kwargs["text"],
                node=kwargs["node"],
                loc_from=kwargs["loc_from"],
                loc_to=kwargs["loc_to"],
            )
            cmnt.save()
            message = "update successful"
            return HttpResponse(data, content_type="application/json")
        elif method == "GET":  # retrieve all comments
            parent_model = parent_model.objects.get(author=request.user.id)
            data = serializers.serialize("json", parent_model.objects.all())
            return HttpResponse(data, content_type="application/json")
        elif method == "PUT":  # update an existing comment
            data = serializers.serialize(
                "json", parent_model.objects.get(author=request.user.id)
            )
            return HttpResponse(data, content_type="application/json")
        elif method == "DELETE":  # delete an existing comment
            return HttpResponse(data, content_type="application/json")
        else:
            return HttpResponseBadRequest(
                f"This view can not handle method {method}.", status=405
            )
