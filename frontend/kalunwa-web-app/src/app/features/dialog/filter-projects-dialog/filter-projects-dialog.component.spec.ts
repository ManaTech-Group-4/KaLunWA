import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FilterProjectsDialogComponent } from './filter-projects-dialog.component';

describe('FilterProjectsDialogComponent', () => {
  let component: FilterProjectsDialogComponent;
  let fixture: ComponentFixture<FilterProjectsDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FilterProjectsDialogComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FilterProjectsDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
