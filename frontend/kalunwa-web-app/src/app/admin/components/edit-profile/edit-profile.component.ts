import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ActivatedRoute, Router } from '@angular/router';
import { first } from 'rxjs/operators';
import { Profile, ProfileReceive } from '../../model/user-model';
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
  isNewImage = false;
  filename = "";
  profileImage:string;
  submitted= false;
  submittedPass = false;
  loading = false;
  loadingPass = false;
  selectedProfile:ProfileReceive;
  userId:string | null;

  constructor(
    private formBuilder: FormBuilder,
    private service: AuthService,
    private router: Router,
    private route: ActivatedRoute,
    private snackBar: MatSnackBar
  ) { }

  ngOnInit(): void {
    this.userId = this.route.snapshot.paramMap.get("id");
    this.profileImage = "../../assets/images/person-icon.jpg";
    const userSubscribe = this.service.getUserById(this.userId).subscribe(
      data =>{
        this.profile.patchValue(data);
      this.selectedProfile = data;
      this.profileImage = this.selectedProfile.image;
      userSubscribe.unsubscribe();
      }
    );

    this.profile = this.formBuilder.group({
      image: [],
      first_name:['', Validators.required],
      last_name:['', Validators.required],
      username:['', Validators.required],
      email:['', [Validators.required, Validators.email]]
    });

    this.updatePass = this.formBuilder.group({
      oldpassword:['', [Validators.required, Validators.minLength(8)]],
      newpassword:['', [Validators.required, Validators.minLength(8)]],
      repassword:['', [Validators.required]]
    },
      {validators: CustomValidators.mustMatch('newpassword', 'repassword')}
    );

  }

  get f() { return this.profile.controls;}

  get form2() { return this.updatePass.controls;}



  onSubmitDetails(imageInput:any){
    // stop here if form is invalid
    if (!this.f.email.valid) {
      this.submitted = true;
      return;
    }

    this.loading = true;
    this.profile.disable();
    const file: File = imageInput.files[0];

    var newAdmin = new FormData();
    newAdmin.append('first_name',this.f.first_name.value);
    newAdmin.append('last_name',this.f.last_name.value);
    newAdmin.append('username',this.f.username.value);
    if(this.isNewImage)
    newAdmin.append('image',file);
    newAdmin.append('email',this.f.email.value);



    const editSubscribe = this.service.updateUser(newAdmin, this.userId)
    .pipe(first())
    .subscribe(
        () => {
          this.router.navigateByUrl("admin/admin-list");
          editSubscribe.unsubscribe();
          this.snackBar.open(`Successfully Updated ${this.f.username.value}'s details`, `Close`, {duration: 3000});
        },
        (err) => {
          this.submitted = true;
          this.loading = false;
          this.profile.enable();
          this.profile.controls["email"].setErrors({'incorrect': true});
          editSubscribe.unsubscribe();
        });


  }

  OnChangePass(){
    this.updatePass.controls["oldpassword"].setErrors({'incorrect': false});
    // stop here if form is invalid
    if (this.form2.invalid) {
      this.submittedPass = true;
      return;
    }

    this.loadingPass = true;
    this.updatePass.disable();

    var newPass = new FormData();
    newPass.append('password',this.form2.oldpassword.value);
    newPass.append('new_password',this.form2.newpassword.value);



    const editSubscribe = this.service.updatePassword(newPass, this.userId)
    .pipe(first())
    .subscribe(
        () => {
          this.router.navigateByUrl("admin/admin-list");
          this.snackBar.open(`Successfully Updated ${this.f.username.value}'s password`, `Close`, {duration: 3000});
          editSubscribe.unsubscribe();
        },
        (err) => {
          this.loadingPass = false;
          this.updatePass.enable();
          this.updatePass.controls["oldpassword"].setErrors({'incorrect': true});
        });


  }

  //inserting file in image input
  onFileChange(imageInput:any){
    const file: File = imageInput.files[0];

    if(!this.isFileImage(file)){
      this.profile.controls["image"].setErrors({'incorrect': true});
      return;
    }
    else{
      this.profile.controls["image"].setErrors(null);

      this.filename = file.name;
      this.isNewImage = true;
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
    return this.f.email.hasError('email') ? 'Not a valid email' : 'Email already exists';
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
