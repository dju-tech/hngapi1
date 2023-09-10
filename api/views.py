from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
import time

class SlackView(APIView):

  def get(self, request):
    track = request.query_params.get('track', '')
    slack_name = request.query_params.get('slack_name', '')
    today = datetime.date.today()
    day = today.strftime("%A")

    current_utc_time = datetime.datetime.utcnow()
    time.sleep(2)

    data = {
      'slack_name' : slack_name,
      'current_day' : day,
      'utc_time' : datetime.datetime.utcnow(),
      'track' : track,
      "github_file_url": "",
      "github_repo_url": "",
      "status_code": 200
    }
    return Response(data)