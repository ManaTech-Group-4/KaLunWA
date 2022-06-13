import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatDialogModule } from '@angular/material/dialog';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { RouterTestingModule } from '@angular/router/testing';
import { routes } from 'src/app/app-routing.module';

import { EditCollectiveComponent } from './edit-collective.component';

describe('EditCollectiveComponent', () => {
  let component: EditCollectiveComponent;
  let fixture: ComponentFixture<EditCollectiveComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditCollectiveComponent ],
      imports: [ReactiveFormsModule, FormsModule, MatDialogModule, HttpClientTestingModule, MatSnackBarModule,RouterTestingModule.withRoutes(routes)]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EditCollectiveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

});
