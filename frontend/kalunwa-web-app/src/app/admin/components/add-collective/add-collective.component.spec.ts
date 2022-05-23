import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddCollectiveComponent } from './add-collective.component';

describe('AddCollectiveComponent', () => {
  let component: AddCollectiveComponent;
  let fixture: ComponentFixture<AddCollectiveComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddCollectiveComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AddCollectiveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
