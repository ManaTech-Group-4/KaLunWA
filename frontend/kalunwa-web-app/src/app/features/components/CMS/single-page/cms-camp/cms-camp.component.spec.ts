import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CmsCampComponent } from './cms-camp.component';

describe('CmsCampComponent', () => {
  let component: CmsCampComponent;
  let fixture: ComponentFixture<CmsCampComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CmsCampComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CmsCampComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
