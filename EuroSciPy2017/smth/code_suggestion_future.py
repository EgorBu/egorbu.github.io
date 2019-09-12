from djang.db i
              >>> import models
              from django.utils.encoding import \
                  python_2_unicode_compatible

              @python_2_unicode_compatible
              class test_from_model(models.Model):
                  title = models.CharField(max_length=100)
