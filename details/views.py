from .models import PlayerWeekdetails, Match, News, Season, Month

from .serializers import PlayerRankingSerializer, MatchSerializer, NewsSerializer, SeasonSerializer, MonthSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


class PlayerRankingView(APIView):

    permission_classes = [AllowAny and IsAuthenticated]
    def get(self, request):
        players = PlayerWeekdetails.objects.all().order_by('-points', '-goals', 'matches')
        serializer = PlayerRankingSerializer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


    permission_classes = [IsAuthenticated and IsAdminUser]
    def post(self, request):
        if not request.user.is_staff:
            return Response({"detail": "Only admin users can add players."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = PlayerRankingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    permission_classes = [IsAuthenticated and IsAdminUser]
    def put(self, request):
        if not request.user.is_staff:
            return Response({"detail": "Only admin users can update players."}, status=status.HTTP_403_FORBIDDEN)
        
        data = request.data
        pk = data.get('id')
        try:
            player = PlayerWeekdetails.objects.get(pk=pk)
        except PlayerWeekdetails.DoesNotExist:
            return Response({"detail": "Player not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlayerRankingSerializer(player, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    permission_classes = [IsAuthenticated and IsAdminUser]
    def patch(self, request):
        if not request.user.is_staff:
            return Response({"detail": "Only admin users can update players."}, status=status.HTTP_403_FORBIDDEN)
        

        data = request.data
        pk = data.get('id')
        try:
            player = PlayerWeekdetails.objects.get(pk=pk)
        except PlayerWeekdetails.DoesNotExist:
            return Response({"detail": "Player not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlayerRankingSerializer(player, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    permission_classes = [IsAuthenticated and IsAdminUser]
    def delete(self, request):
        if not request.user.is_staff:
            return Response({"detail": "Only admin users can delete players."}, status=status.HTTP_403_FORBIDDEN)
        
        data = request.data
        pk = data.get('id')
        try:
            player = PlayerWeekdetails.objects.get(pk=pk)
        except PlayerWeekdetails.DoesNotExist:
            return Response({"detail": "Player not found."}, status=status.HTTP_404_NOT_FOUND)

        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class MatchListView(APIView):
    permission_classes = [AllowAny and IsAuthenticated]

    def get(self, request):
        matches = Match.objects.all().order_by('-date', '-time')
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


    permission_classes = [IsAuthenticated and IsAdminUser]
    def post(self, request):
        if not request.user.is_staff:
            return Response({"detail": "Only admin users can add matches."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    permission_classes = [IsAuthenticated and IsAdminUser]
    def put(self, request):
        if not request.user.is_staff:
            return Response({"detail": "Only admin users can update matches."}, status=status.HTTP_403_FORBIDDEN)
        

        data = request.data
        pk = data.get('id')
        try:
            match = Match.objects.get(pk=pk)
        except Match.DoesNotExist:
            return Response({"detail": "Match not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MatchSerializer(match, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    permission_classes = [IsAuthenticated and IsAdminUser]
    def patch(self, request):
        if not request.user.is_staff:
            return Response({"detail": "Only admin users can update matches."}, status=status.HTTP_403_FORBIDDEN)


        data = request.data
        pk = data.get('id')     
        try:
            match = Match.objects.get(pk=pk)
        except Match.DoesNotExist:
            return Response({"detail": "Match not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MatchSerializer(match, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    parser_classes = [IsAuthenticated and IsAdminUser]
    def delete(self, request):
        if not request.user.is_staff:
            return Response({"detail": "Only admin users can delete matches."}, status=status.HTTP_403_FORBIDDEN)


        data = request.data
        pk = data.get('id')
        try:
            match = Match.objects.get(pk=pk)
        except Match.DoesNotExist:
            return Response({"detail": "Match not found."}, status=status.HTTP_404_NOT_FOUND)

        match.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class NewsListView(APIView):
    permission_classes = [AllowAny and IsAuthenticated]
    def get(self, request):
        news = News.objects.all().order_by('-created_at')
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    permission_classes = [IsAuthenticated and IsAdminUser]
    def post(self, request):
        if not request.user.is_staff:
            return Response({"detail": "Only admin users can add news."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    permission_classes = [IsAuthenticated and IsAdminUser]
    def put(self, request):
        if not request.user.is_staff:
            return Response({"detail": "Only admin users can update news."}, status=status.HTTP_403_FORBIDDEN)


        data = request.data
        pk = data.get('id')
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response({"detail": "News not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = NewsSerializer(news, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    permission_classes = [IsAuthenticated and IsAdminUser]
    def patch(self, request):   
        if not request.user.is_staff:
            return Response({"detail": "Only admin users can update news."}, status=status.HTTP_403_FORBIDDEN)



        data = request.data
        pk = data.get('id')
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response({"detail": "News not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = NewsSerializer(news, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



    permission_classes = [IsAuthenticated and IsAdminUser]
    def delete(self, request):
        if not request.user.is_staff:
            return Response({"detail": "Only admin users can delete news."}, status=status.HTTP_403_FORBIDDEN)
        
        data = request.data
        pk = data.get('id')
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response({"detail": "News not found."}, status=status.HTTP_404_NOT_FOUND)

        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



class SeasonListView(APIView):
    permission_classes = [AllowAny and IsAuthenticated]
    def get(self, request):
        seasons = Season.objects.all().order_by('-season_year')
        serializer = SeasonSerializer(seasons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = SeasonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        data = request.data
        pk = data.get('id')
        try:
            season = Season.objects.get(pk=pk)
        except Season.DoesNotExist:
            return Response({"detail": "Season not found."}, status=status.HTTP_404_NOT_FOUND)

        season.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



class MonthListView(APIView):
    permission_classes = [AllowAny and IsAuthenticated]
    def get(self, request):
        months = Month.objects.all().order_by('-month_name')
        serializer = MonthSerializer(months, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MonthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        data = request.data
        pk = data.get('id')
        try:
            month = Month.objects.get(pk=pk)
        except Month.DoesNotExist:
            return Response({"detail": "Month not found."}, status=status.HTTP_404_NOT_FOUND)

        month.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

