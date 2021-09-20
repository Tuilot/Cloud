from django import forms


class OjInfoForm(forms.Form):
    oj_name = forms.CharField(label='OJ名：', widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'oj_name'}
    ))
    pages = forms.IntegerField(label='总页数：', widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'pages'}
    ))
    problems_count = forms.IntegerField(label='总问题数：', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'problems_count'}
    ))
    oj_url = forms.CharField(label='OJ链接：', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'oj_url'}
    ))


class AnnouncementForm(forms.Form):
    title = forms.CharField(label='公告标题', widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'announcement-title'}
    ))
    content = forms.CharField(label='公告内容', widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'announcement-content', 'rows': 5}
    ))
