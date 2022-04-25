import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IndiEventComponent } from './indi-event.component';

describe('IndiEventComponent', () => {
  let component: IndiEventComponent;
  let fixture: ComponentFixture<IndiEventComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ IndiEventComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(IndiEventComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
