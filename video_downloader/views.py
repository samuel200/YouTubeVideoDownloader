from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pafy

def home(request):
    return render(request, 'index.html', {})

def video_details(request, youtube_url):
    try:
        source = pafy.new(youtube_url)
    
    except Exception:
        return JsonResponse({"error_message": "Error in getting video details."})

    resolutions = [i.resolution[-3:] for i in source.streams]
    extensions = [i.extension for i in source.streams]
    response = {"resolutions": resolutions, "extensions": extensions}
    return JsonResponse(response)

def video_stream_details(request, youtube_url, extension, resolution):
    try:
        source = pafy.new(youtube_url)
    
    except Exception:
        return JsonResponse({"error-message": "Error in getting video details."})

    stream = list(filter(lambda x: x.resolution[-3:] == resolution and x.extension == extension, source.streams))[0]
    response = {
        "title": source.title,
        "image": source.thumb,
        "size": f"{ round(stream.get_filesize() / 1048579.37516484, 2) }mb",
        "download_url": stream.url
    }

    return JsonResponse(response)