import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { first } from 'rxjs/operators';
import { AuthService } from '../../service/auth.service';
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
    this.loading = true;
    this.profile.disable();

    // stop here if form is invalid
    if (this.profile.invalid) {
      return;
    }

    this.service.register(this.f.email.value, this.f.password.value)
    .pipe(first())
    .subscribe(
        data => {
          this.router.navigateByUrl("admin/admin-list");
        },
        error => {
          this.loading = false;
          this.profile.enable();
        });

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
