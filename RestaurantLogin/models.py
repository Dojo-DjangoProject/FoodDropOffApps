from django.db import models
import re
# import bcrypt

class RestaurantManager(models.Manager):
    def register_validator(self,postData):
        errors = {}
        not_blank = "This field cannot be left blank."
        fewer_2 = "This field cannot be fewer than 2 characters in length."
        longer_3 = "This field cannot be longer than 30 characters in length."
        invalid_email = "Invalid email address."
        
        # Name Validations
        if len(postData['name']) == 0:
            errors['name'] = not_blank
        elif len(postData['name']) < 2:
            errors['name'] = fewer_2
        elif len(postData['name']) > 30:
            errors['name'] = longer_3

        # Owner Name Validations
        if len(postData['owner']) == 0:
            errors['owner'] = not_blank
        elif len(postData['owner']) < 2:
            errors['owner'] = fewer_2
        elif len(postData['owner']) > 30:
            errors['owner'] = longer_3

        # Address Validations
        if len(postData['address']) == 0:
            errors['address'] = not_blank
        elif len(postData['address']) < 2:
            errors['address'] = fewer_2
        elif len(postData['address']) > 100:
            errors['address'] = longer_3


        # Include Birthday Validations

        # Email Validations
        EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
        user = User.objects.filter(email_address=postData['email'])
        if len(postData['email']) == 0:
            errors['email'] = not_blank
        elif len(postData['email']) < 6:
            errors['email'] = invalid_email
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = invalid_email
        elif user:
            errors['email'] = "Please use another email address."

        # Password Registration Validations
        PASS_REGEX = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,16}$")
        if len(postData['pword']) == 0:
            errors['pword'] = not_blank
        elif len(postData['pword_confirm']) == 0:
            errors['pword_confirm'] = not_blank
        elif len(postData['pword']) < 8:
            errors['pword'] = "Password must be at least 8 characters long."
        elif not PASS_REGEX.match(postData['pword']):
            errors['pword'] = "Password must contain 1 uppercase, 1 lowercase, 1 number, and 1 special character."
        elif postData['pword'] != postData['pword_confirm']:
            errors['pword_confirm'] = "Passwords do not match."
        
        return errors

    def login_validator(self,postData):
        errors = {}
        user_pass = 'Email/Password is incorrect or User does not exist'
        user = User.objects.filter(email_address=postData['email'])
        if not user:
            errors['login'] = user_pass
        elif not bcrypt.checkpw(postData['login_pword'].encode(), user[0].password.encode()):
            errors['login'] = user_pass

        return errors

    def update_validator(self,postData):
        
        errors = {}
        not_blank = "This field cannot be left blank."
        fewer_2 = "This field cannot be fewer than 2 characters in length."
        longer_3 = "This field cannot be longer than 30 characters in length."
        invalid_email = "Invalid email address."
        
        # First Name Validations
        if len(postData['name']) == 0:
            errors['name'] = not_blank
        elif len(postData['name']) < 2:
            errors['name'] = fewer_2
        elif len(postData['name']) > 30:
            errors['name'] = longer_3

        # Owner Name Validations
        if len(postData['owner']) == 0:
            errors['owner'] = not_blank
        elif len(postData['owner']) < 2:
            errors['owner'] = fewer_2
        elif len(postData['owner']) > 30:
            errors['owner'] = longer_3

        # # Address Validations
        # if len(postData['address']) == 0:
        #     errors['address'] = not_blank
        # elif len(postData['address']) < 2:
        #     errors['address'] = fewer_2
        # elif len(postData['address']) > 100:
        #     errors['address'] = longer_3

        # Email Validations
        EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
        user = User.objects.filter(email_address=postData['email'])
        if len(postData['email']) == 0:
            errors['email'] = not_blank
        elif len(postData['email']) < 6:
            errors['email'] = invalid_email
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = invalid_email
        elif user:
            errors['email'] = "Please use another email address."

        return errors

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    cuisine = models.CharField(max_length=50)

    # location = models.ForeignKey(Location, related_name="location_restaurants", on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=10)
    email_address = models.CharField(max_length=50)
    password = models.CharField(max_length = 70)
    # events: All events assocated with this restaurant
    # menus: All menus assocated with this restaurant
    # items: All items assocated with this restaurant

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = RestaurantManager()

    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # email = models.CharField(max_length=50)
    # password = models.CharField(max_length=70)
    # restaurant_name = models.CharField(max_length=255)
    # cuisine = models.CharField(max_length=50)
    # phone_number = models.CharField(max_length=10)
    # location = models.ForeignKey(Location, related_name="location_restaurants", on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)