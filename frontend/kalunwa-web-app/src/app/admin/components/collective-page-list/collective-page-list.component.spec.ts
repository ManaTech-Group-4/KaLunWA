import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ComponentFixture, inject, TestBed } from '@angular/core/testing';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatDialogModule } from '@angular/material/dialog';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { RouterTestingModule } from '@angular/router/testing';
import { routes } from 'src/app/app-routing.module';
import { CollectivePagesService } from '../../service/collective-pages.service';

import { CollectivePageListComponent } from './collective-page-list.component';

describe('CollectivePageListComponent', () => {
  let component: CollectivePageListComponent;
  let fixture: ComponentFixture<CollectivePageListComponent>;
  let testBedService: CollectivePagesService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CollectivePageListComponent ],
      imports:[HttpClientTestingModule, MatDialogModule, RouterTestingModule.withRoutes(routes), MatSnackBarModule]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CollectivePageListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();

    testBedService = TestBed.get(CollectivePagesService);
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });



});
