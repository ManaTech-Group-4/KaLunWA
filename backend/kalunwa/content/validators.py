from rest_framework import serializers

# # validate if start_date is less than or equal to end date
def validate_start_date_and_end_date(start_date, end_date):
    # if end date is not null and ...
    if end_date and start_date > end_date: 
        raise serializers.ValidationError(
            'Start date must be earlier, or the same as the end date.')
    