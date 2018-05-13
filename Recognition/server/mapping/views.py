import base64

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from server.info.settings import MEDIA_ROOT
import FacialRecognition.FaceRecognition as FR


@csrf_exempt
def photo(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        image = base64.b64decode(file.read())
        with open(MEDIA_ROOT + "/img.jpg", "wb") as f:
            f.write(image)
        return HttpResponse(FR.face_recognizer(MEDIA_ROOT + "/img.jpg"))
    return HttpResponse("ERROR")
