import { ComponentFixture, TestBed } from '@angular/core/testing';
import { MatDesignModule } from '../../shared/mat-design.module';

import { AboutCampComponent } from './about-camp.component';

describe('AboutCampComponent', () => {
  let component: AboutCampComponent;
  let fixture: ComponentFixture<AboutCampComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AboutCampComponent ],
      imports: [ MatDesignModule ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AboutCampComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
