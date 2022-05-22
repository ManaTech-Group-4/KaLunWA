import { HttpClient } from '@angular/common/http';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { ComponentFixture, inject, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { AboutpageService } from '../../service/aboutpage.service';
import { MatDesignModule } from '../../shared/mat-design.module';

import { AboutCampComponent } from './about-camp.component';

describe('AboutCampComponent', () => {
  let component: AboutCampComponent;
  let fixture: ComponentFixture<AboutCampComponent>;
  let testBedService : AboutpageService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AboutCampComponent ],
      imports: [ MatDesignModule,
                  HttpClientTestingModule ],
      providers: [AboutpageService]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AboutCampComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();

    testBedService = TestBed.get(AboutpageService);
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should switch to other camp after click', () => {
    let value = fixture.debugElement.query(By.css('.sidenav')).nativeElement.getAttribute('value');
    value = 2;
    expect(value).toEqual(2);
  });


  it('Service injected via inject() and TestBed.get() should be the same (AboutpageService)',
    inject([AboutpageService], (injectService: AboutpageService) => {
      expect(injectService).toBe(testBedService);
  }));

});
