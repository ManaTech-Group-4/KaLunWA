import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CmsGalleryComponent } from './cms-gallery.component';

describe('CmsGalleryComponent', () => {
  let component: CmsGalleryComponent;
  let fixture: ComponentFixture<CmsGalleryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CmsGalleryComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CmsGalleryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
