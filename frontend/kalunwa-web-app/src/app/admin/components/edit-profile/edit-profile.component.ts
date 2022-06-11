import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { first } from 'rxjs/operators';
import { AuthService } from '../../service/auth.service';
import { CustomValidators } from '../../shared/customValidation';

@Component({
  selector: 'app-edit-profile',
  templateUrl: './edit-profile.component.html',
  styleUrls: ['./edit-profile.component.scss']
})
export class EditProfileComponent implements OnInit {
  profile: FormGroup;
  updatePass: FormGroup;
  isAdd = false;
  filename = "";
  profileImage:string;
  submitted= false;
  loading = false;

  constructor(
    private formBuilder: FormBuilder,
    private service: AuthService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.profile = this.formBuilder.group({
      image: [null],
      firstname:['', Validators.required],
      lastname:['', Validators.required],
      username:['', Validators.required],
      email:['', [Validators.required, Validators.email]]
    }
    );

    this.updatePass = this.formBuilder.group({
      oldpassword:['', [Validators.required, Validators.minLength(8)]],
      newpassword:['', [Validators.required, Validators.minLength(8)]],
      repassword:['', [Validators.required]]
    },
      {validators: CustomValidators.mustMatch('newpassword', 'repassword')}
    );

    this.profileImage = "../../assets/images/person-icon.jpg";
  }

  get f() { return this.profile.controls;}

  get form2() { return this.updatePass.controls;}



  onSubmit(){
    this.submitted = true;
    this.loading = true;
    this.profile.disable();

    // stop here if form is invalid
    if (this.profile.invalid) {
      return;
    }


  }


  onFileChange(imageInput:any){
    const file: File = imageInput.files[0];

    if(!this.isFileImage(file)){
      this.profile.controls["image"].setErrors({'incorrect': true});
      return;
    }
    else{
      this.profile.controls["image"].setErrors(null);

      this.filename = file.name;
      console.log(this.filename)
    }


    if(imageInput.files && imageInput.files.length > 0){
      const imgFile = imageInput.files[0];
      // File Preview
      const reader = new FileReader();
      reader.onload = () => {
        this.profileImage = reader.result as string;
      }
      reader.readAsDataURL(imgFile)
    }
  }

  // Image Preview
  showPreview(event:any) {
    const file = event.target.files[0];
    this.profile.patchValue({
      image: file
    });
    this.profile.get('image')!.updateValueAndValidity()
    // File Preview
    const reader = new FileReader();
    reader.onload = () => {
      this.profileImage = reader.result as string;
    }
    reader.readAsDataURL(file)
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
    if (this.form2.newpassword.hasError('required')) {
      return 'Password is required';
    }

    return this.form2.newpassword.invalid ? 'Password must atleast be 8 characters' : '';
  }
  getErrorRepassMessage() {
    if (this.form2.repassword.hasError('required')) {
      return 'Confirm Password is required';
    }

    return this.form2.repassword.hasError('mustMatch') ? 'Password and confirm password not match' : '';
  }

}
