from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime

class SlackView(APIView):

  def get(self, request):
    track = request.query_params.get('track', '')
    slack_name = request.query_params.get('slack_name', '')
    today = datetime.date.today()
    day = today.strftime("%A")

    current_utc_time = datetime.datetime.utcnow()
    formatted_utc_time = current_utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    data = {
      'slack_name' : slack_name,
      'current_day' : day,
      'utc_time' : formatted_utc_time,
      'track' : track,
      "github_file_url": "https://github.com/eletrikode/hngapi1/blob/main/api/views.py",
      "github_repo_url": "https://github.com/eletrikode/hngapi1",
      "status_code": 200
    }
    return Response(data)
