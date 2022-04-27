import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IndivProjectComponent } from './indiv-project.component';

describe('IndivProjectComponent', () => {
  let component: IndivProjectComponent;
  let fixture: ComponentFixture<IndivProjectComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ IndivProjectComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(IndivProjectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
