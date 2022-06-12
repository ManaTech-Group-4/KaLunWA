import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatDialogModule } from '@angular/material/dialog';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { RouterTestingModule } from '@angular/router/testing';
import { routes } from 'src/app/app-routing.module';

import { EditProfileComponent } from './edit-profile.component';

describe('EditProfileComponent', () => {
  let component: EditProfileComponent;
  let fixture: ComponentFixture<EditProfileComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditProfileComponent ],
      imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule, MatDialogModule, RouterTestingModule.withRoutes(routes), MatSnackBarModule]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EditProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });


  it('should require valid email', () => {
    component.f.email.setValue({
      "email": "invalidemail"
    });

    expect(component.f.email.valid).toEqual(false);
  });


  it('password and confirm password should match', () => {
    component.form2.newpassword.setValue(
      {'newpassword': "adasdasdasd"}
    );
    component.form2.repassword.setValue(
      {'repassword': "aaadasdasdasd"}
    );

    expect(component.form2.repassword.valid).toEqual(false);
  });
});
