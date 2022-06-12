import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditCollectiveComponent } from './edit-collective.component';

describe('EditCollectiveComponent', () => {
  let component: EditCollectiveComponent;
  let fixture: ComponentFixture<EditCollectiveComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditCollectiveComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EditCollectiveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
