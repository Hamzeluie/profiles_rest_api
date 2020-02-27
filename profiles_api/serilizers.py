from rest_framework import serializers


class HelloSerilizers(serializers.Serializer):
    """serializes a name filed for testing api view"""
    name = serializers.CharField(max_length=10)

