from rest_framework.decorators import api_view
from rest_framework.response import Response
from pytube import YouTube
from django.http import JsonResponse

@api_view(['POST'])  # Correct usage of the decorator
def download_video(request):
    url = request.data.get('url')
    if not url:
        return JsonResponse({'error': 'No URL provided'}, status=400)

    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()  # Specify a path if needed
        return JsonResponse({'message': 'Video downloaded successfully!'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

