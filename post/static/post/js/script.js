var form_fields = Document.getElementByTagName('input')
    form_fields[1].placeholder = 'Username';
    form_fields[2].placeholder = 'Email';
    form_fields[3].placeholder = 'Password';
    form_fields[4].placeholder = 'Password Cornfirmation';


    for (var field in form_fields) {
        form_fields[field].className += ' form-control'
    }