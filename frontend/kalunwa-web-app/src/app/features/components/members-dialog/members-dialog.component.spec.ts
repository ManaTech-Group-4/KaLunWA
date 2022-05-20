import { HttpClientModule } from '@angular/common/http';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';

import { MembersDialogComponent } from './members-dialog.component';

describe('MembersDialogComponent', () => {
  let component: MembersDialogComponent;
  let fixture: ComponentFixture<MembersDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MembersDialogComponent ],
      imports: [ HttpClientModule],
      providers: [
        { provide: MAT_DIALOG_DATA, useValue: {} },
        { provide: MatDialogRef, useValue: {} }
    ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MembersDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

});
