from django import forms

from .models import Post, CVPost, CVPostExperience, CVPostSkils


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CVPostForm(forms.ModelForm):

    class Meta:
        model = CVPost
        fields = ('title', 'text',)


class CVPostExperienceForm(forms.ModelForm):

    class Meta:
        model = CVPostExperience
        fields = ('title', 'text',)


class CVPostSkillsForm(forms.ModelForm):

    class Meta:
        model = CVPostSkils
        fields = ('title', 'text',)
