from django.contrib import admin
from .models import Post
from .models import CVPost
from .models import CVPostExperience
from .models import CVPostSkils

admin.site.register(Post)
admin.site.register(CVPost)
admin.site.register(CVPostExperience)
admin.site.register(CVPostSkils)


