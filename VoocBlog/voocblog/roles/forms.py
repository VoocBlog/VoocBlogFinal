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
        widgets = {
            'title_post': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Tiêu Đề Bài Viết...'}),
            'body_post': forms.Textarea(attrs={'class': 'new-class-name two', 'placeholder':'Nội Dung Bài Viết...',"cols": 82, "rows":19, 'style': 'padding: 10px; border-radius: 5px'}),
            'image_post': forms.FileInput(attrs={'class': 'form-control', 'placeholder':'Tải Hình Ảnh Lên', 'style': 'height: 45px'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder':'Chọn Thể Loại', 'style': 'margin-bottom: 20px'}),
        }
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