import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DummyLandingComponent } from './dummy-landing.component';

describe('DummyLandingComponent', () => {
  let component: DummyLandingComponent;
  let fixture: ComponentFixture<DummyLandingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DummyLandingComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DummyLandingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
