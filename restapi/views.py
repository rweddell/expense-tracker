from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from restapi import models, serializers
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView


class ExpenseListCreate(ListCreateAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
    # def get(self, request):
    #     expenses = models.Expense.objects.all()
    #     # all_expenses = [model_to_dict(expense) for expense in expenses]
    #     serial = serializers.Expense(expenses, many=True)
    #     return Response(serial.data, 200)
    #
    # def post(self, request):
    #     serial = serializers.Expense(data=request.data)
    #     serial.is_valid(raise_exception=True)
    #     serial.save()
    #     return Response(serial.data, status=201)


class ExpenseRetrieveDelete(RetrieveDestroyAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
    # def get(self, request, pk):
    #     return Response()
    #
    # def post(self, request):
    #     return Response()
