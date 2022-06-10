import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CustomValidators } from '../../shared/customValidation';

@Component({
  selector: 'app-add-profile',
  templateUrl: './add-profile.component.html',
  styleUrls: ['./add-profile.component.scss']
})
export class AddProfileComponent implements OnInit {
  profile: FormGroup;
  isAdd = false;
  filename = "";
  profileImage:any;
  submitted= false;
  loading = false;

  constructor(
    private formBuilder: FormBuilder
  ) { }

  ngOnInit(): void {
    this.profile = this.formBuilder.group({
      image: [null],
      firstname:['', Validators.required],
      lastname:['', Validators.required],
      email:['', [Validators.required, Validators.email]],
      password:['', [Validators.required, Validators.minLength(8)]],
      repassword:['', [Validators.required]]
    },
      {validators: CustomValidators.mustMatch('password', 'repassword')}
    );

    this.profileImage = "../../assets/images/person-icon.jpg";
  }

  get f() { return this.profile.controls;}

  onSubmit(){
    this.submitted = true;

    // stop here if form is invalid
    if (this.profile.invalid) {
      return;
    }

    this.loading = true;
    this.submitted = true;
    console.log("submitted");

  }


  onFileChange(imageInput:any){
    const file: File = imageInput.files[0];
    const reader = new FileReader();
    if(!this.isFileImage(file))
      this.profile.controls["image"].setErrors({'incorrect': true});
    else{
      this.profile.controls["image"].setErrors(null);

      this.filename = file.name;
    }
  }

  isFileImage(file: File) {
    return file && file['type'].split('/')[0] === 'image';
  }


  getErrorMessage() {
    if (this.f.email.hasError('required')) {
      return 'You must enter a value';
    }

    return this.f.email.hasError('email') ? 'Not a valid email' : '';
  }
  getErrorPassMessage() {
    if (this.f.password.hasError('required')) {
      return 'Password is required';
    }

    return this.f.password.invalid ? 'Password must atleast be 8 characters' : '';
  }
  getErrorRepassMessage() {
    if (this.f.repassword.hasError('required')) {
      return 'Confirm Password is required';
    }

    return this.f.repassword.hasError('mustMatch') ? 'Password and confirm password not match' : '';
  }

}
