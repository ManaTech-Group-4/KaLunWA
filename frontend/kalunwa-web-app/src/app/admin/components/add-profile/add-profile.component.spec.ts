import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatDialogModule } from '@angular/material/dialog';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { RouterTestingModule } from '@angular/router/testing';
import { routes } from 'src/app/app-routing.module';

import { AddProfileComponent } from './add-profile.component';

describe('AddProfileComponent', () => {
  let component: AddProfileComponent;
  let fixture: ComponentFixture<AddProfileComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddProfileComponent ],
      imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule, MatDialogModule, RouterTestingModule.withRoutes(routes), MatSnackBarModule]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AddProfileComponent);
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
    component.f.password.setValue(
      {'password': "adasdasdasd"}
    );
    component.f.repassword.setValue(
      {'repassword': "aaadasdasdasd"}
    );

    expect(component.f.repassword.valid).toEqual(false);
  });

});
