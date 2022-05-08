import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LasangComponent } from './lasang.component';

describe('LasangComponent', () => {
  let component: LasangComponent;
  let fixture: ComponentFixture<LasangComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LasangComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LasangComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
