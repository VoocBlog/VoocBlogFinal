from django import forms


from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title_post',
            'body_post',
            'image_post',
            'category'
        ]

# class abc(forms .Form):
#     title_post = forms.CharField(label='Account', max_length=30)
#     body_post = forms.CharField(label='Body post', max_length=30)
#     category = forms.CharField(label='Category', max_length=30)
#     image_post = 'images/images/200_5TI0RKc.jpg'
    
#     def save(self):
#         Post.objects.create_user(title_post=self.cleaned_data['title_post'], body_post=self.cleaned_data['body_post'], category=self.cleaned_data['category'], image_post=self.cleaned_data['image_post'])

#class PostForm(forms.Form):
#    title_post = forms.CharField(max_length=300)
#    body_post = forms.CharField()
#    image_post = forms.ImageField()
#    category = forms.CharField()



