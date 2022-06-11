import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { first } from 'rxjs/operators';
import { Profile } from '../../model/user-model';
import { AuthService } from '../../service/auth.service';
import { CollectivePagesService } from '../../service/collective-pages.service';
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
  imgFile: any;

  constructor(
    private formBuilder: FormBuilder,
    private service: AuthService,
    private router: Router,
    private cd: ChangeDetectorRef,
    private colservice: CollectivePagesService
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



  onSubmit(imageInput:any){

    const file: File = imageInput.files[0];
    console.log(file, this.f);
    var newAdmin = new FormData();
    newAdmin.append('first_name',this.f.firstname.value);
    newAdmin.append('last_name',this.f.lastname.value);
    newAdmin.append('username',this.f.username.value);
    newAdmin.append('email',this.f.email.value);
    newAdmin.append('password',this.f.password.value);
    newAdmin.append('image',this.f.image.value);
    //  ={
    //   "first_name": this.f.firstname.value,
    //   "last_name": this.f.lastname.value,
    //   "username": this.f.username.value,
    //   "email": this.f.email.value,
    //   "password": this.f.password.value,
    //   "image": this.f.image.value

    // };
    console.log(newAdmin);
    this.submitted = true;
    this.loading = true;
    this.profile.disable();

    // stop here if form is invalid
    if (this.profile.invalid) {
      return;
    }


    this.service.register(newAdmin)
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
    const reader = new FileReader();
    const file: File = imageInput.target.files[0];

    if(!this.isFileImage(file)){
      this.profile.controls["image"].setErrors({'incorrect': true});
      return;
    }
    else{
      this.profile.controls["image"].setErrors(null);

      this.filename = file.name;

      this.colservice.uploadImage(this.filename,file).subscribe(
        (res) => {
        },
        (err) => {

        });

    }
    if(imageInput.target.files && imageInput.target.files[0]){
      // File Preview
      reader.readAsDataURL(file);

      reader.onload = () => {
        this.profileImage = reader.result as string;
        this.profile.patchValue({
          image: reader.result
        });

      }
      // ChangeDetectorRef since file is loading outside the zone
      this.cd.markForCheck();
    }
  }

  // Image Preview
  // showPreview(event:any) {
  //   const file = event.target.files[0];
  //   this.profile.patchValue({
  //     image: file
  //   });
  //   this.profile.get('image')!.updateValueAndValidity()
  //   // File Preview
  //   const reader = new FileReader();
  //   reader.onload = () => {
  //     this.profileImage = reader.result as string;
  //   }
  //   reader.readAsDataURL(file)
  // }


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
