import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { MatDialogModule } from '@angular/material/dialog';

import { AdminListComponent } from './admin-list.component';

describe('AdminListComponent', () => {
  let component: AdminListComponent;
  let fixture: ComponentFixture<AdminListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AdminListComponent ],
      imports: [ HttpClientTestingModule, MatDialogModule]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AdminListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });
});
