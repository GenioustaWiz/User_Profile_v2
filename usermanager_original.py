class UserManager(BaseUserManager):

    def _create_user(self, email, first_name, last_name,  password, is_staff, is_superuser, request=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        if not first_name:
            raise ValueError(_("First name is required"))

        if not last_name:
            raise ValueError(_("Last name is required"))

        # Get IP address from the request
        # ip_address = None
        # if request:
        #     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        #     if x_forwarded_for:
        #         ip_address = x_forwarded_for.split(',')[0]
        #     else:
        #         ip_address = request.META.get('REMOTE_ADDR')

        # # Use GeoIP2 to get the country based on the IP address
            # country = None
            # if ip_address:
            #     g = GeoIP2()
            #     try:
            #         country = g.country(ip_address)['country_code']
            #     except:
            #         pass
        # Generate username based on email if username is empty
        # username = email.split('@')[0]


        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            # ip_address=ip_address,
            # # country=country,
            # username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        # Resize the image
        # img = Image.open(user.image.path)
        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(user.image.path)

        return user

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,first_name,last_name,password, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fieds.setdefault("is_verified", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is staff must be true for admin user')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is superuser must be true for admin user')

        return self._create_user(email,first_name,last_name,password, **extra_fields)
