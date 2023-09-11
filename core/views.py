# myapp/views.py
from django.http import JsonResponse
from datetime import datetime, timedelta
import pytz

def info_endpoint(request):
    # Extract query parameters slack_name and track from the GET request
    slack_name = request.GET.get('slack_name', 'dtechshoemaker')
    track = request.GET.get('track', 'Backend')

    # Get the current day of the week in full
    current_day = datetime.now().strftime('%A')

    # Get the current UTC time with validation of +/-2 minutes
    utc_now = datetime.now(pytz.utc)
    utc_min = utc_now - timedelta(minutes=2)
    utc_max = utc_now + timedelta(minutes=2)

    # Check if the current time is within +/-2 minutes
    if utc_min <= utc_now <= utc_max:
        current_utc_time = utc_now.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return JsonResponse({'error': 'UTC time validation failed'}, status=400)

    # Construct the GitHub URLs based on your project
    github_file_url = 'https://github.com/dtechshoemaker/HNG-intern-task/blob/main/core/views.py'
    github_repo_url = 'https://github.com/dtechshoemaker/HNG-intern-task'
    # Create the response JSON
    data = {
        'slack_name': slack_name,
        'current_day_of_week': current_day,
        'current_utc_time': current_utc_time,
        'track': track,
        'github_url_of_file': github_file_url,
        'github_url_of_source_code': github_repo_url,
        'status_code': 200
    }

    return JsonResponse(data)
