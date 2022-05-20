import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CmsOrgStructComponent } from './cms-org-struct.component';

describe('CmsOrgStructComponent', () => {
  let component: CmsOrgStructComponent;
  let fixture: ComponentFixture<CmsOrgStructComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CmsOrgStructComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CmsOrgStructComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
