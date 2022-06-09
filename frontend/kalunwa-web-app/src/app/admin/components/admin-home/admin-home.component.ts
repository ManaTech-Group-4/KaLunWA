import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { first } from 'rxjs/operators';
import { Admin } from '../../model/user-model';
import { AuthService } from '../../service/auth.service';

@Component({
  selector: 'app-admin-home',
  templateUrl: './admin-home.component.html',
  styleUrls: ['./admin-home.component.scss']
})
export class AdminHomeComponent implements OnInit {

  loginForm: FormGroup;
  loading = false;
  submitted = false;
  isInvalid = false;


  constructor(
        private formBuilder: FormBuilder,
        private authService: AuthService,
        private router: Router) {
        }

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group({
        email: ['', Validators.required],
        password: ['', Validators.required]
    });

    // get return url from route parameters or default to '/'
  }

  get f() { return this.loginForm.controls; }

  onSubmit() {
    this.submitted = true;

    // stop here if form is invalid
    if (this.loginForm.invalid) {
        return;
    }
    this.loginForm.disable();

    this.isInvalid = false;
    this.loading = true;
    this.authService.login(this.f.email.value, this.f.password.value)
        .pipe(first())
        .subscribe(
            data => {
              this.router.navigateByUrl("admin/dashboard");
            },
            error => {
              this.isInvalid = true;
              console.log(this.isInvalid);
              this.loading = false;
              this.loginForm.enable();
            });
  }

  getErrorMessage(field: string): string {
    if(field == "username"){
      if (this.f.email.hasError('required')) {
        return 'Please enter an email';
      }
    }
    if(field == "password"){
      if (this.f.password.hasError('required')) {
        return 'Please enter a password';
      }
    }
    return "";
  }

}
